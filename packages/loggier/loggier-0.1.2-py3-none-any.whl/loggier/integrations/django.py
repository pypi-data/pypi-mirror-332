"""
Django middleware integration for Loggier with comprehensive context capturing.
"""
import uuid
import time
import json
import functools
from typing import Dict, List, Any, Optional, Union, Callable, Set

from django.conf import settings
from django.http import HttpRequest, HttpResponse

# Import Loggier client
from ..client import Loggier

# Global Loggier instance for the middleware
_loggier_instance = None

# Registry for decorated views
_tracked_views = set()

def track_endpoint(tags=None, statuses=None, capture_request_body=False, capture_response_body=False):
    """
    Decorator to track specific endpoints.
    
    Args:
        tags: Additional tags for this endpoint
        statuses: Status codes to track (defaults to all)
        capture_request_body: Whether to capture the full request body (careful with sensitive data)
        capture_response_body: Whether to capture the full response body
        
    Example:
        @track_endpoint(tags=['critical', 'payment'])
        def my_view(request):
            ...
    """
    def decorator(view_func):
        # Register this view function for tracking
        _tracked_views.add(view_func)
        
        # Store tracking options on the function
        view_func._loggier_track_options = {
            'tags': tags or [],
            'statuses': statuses or [],
            'capture_request_body': capture_request_body,
            'capture_response_body': capture_response_body
        }
        
        @functools.wraps(view_func)
        def wrapped_view(*args, **kwargs):
            return view_func(*args, **kwargs)
        
        return wrapped_view
    
    return decorator

class LoggierDjangoMiddleware:
    """
    Django middleware for Loggier integration with comprehensive context capturing.
    
    Add to your Django MIDDLEWARE setting:
    
    MIDDLEWARE = [
        ...
        'loggier.integrations.django.LoggierDjangoMiddleware',
        ...
    ]
    
    And configure in settings.py:
    
    LOGGIER = {
        'API_KEY': 'your-api-key',
        'API_URL': 'https://api.loggier.com/api/ingest',
        'ENVIRONMENT': 'development',
        'TAGS': ['django', 'web'],
        'PROJECT_NAME': 'your-project',
        'CAPTURE_REQUEST_DATA': True,
        'LOG_SLOW_REQUESTS': True,
        'SLOW_REQUEST_THRESHOLD': 1.0,  # seconds
        'STATUSES_TO_TRACK': [500, 400, 401, 403],  # Status codes to track
        'CAPTURE_REQUEST_BODY': False,  # Capture request body for tracked statuses
        'CAPTURE_RESPONSE_BODY': True,  # Capture response body for tracked statuses
        'MAX_BODY_SIZE': 16384,  # Max body size to capture (16KB)
        'INCLUDE_STACKTRACE': True  # Include stacktrace for errors
    }
    """
    
    def __init__(self, get_response):
        """
        Initialize the middleware.
        
        Args:
            get_response: The next middleware or view in the chain
        """
        self.get_response = get_response
        
        # Get configuration from Django settings
        config = getattr(settings, "LOGGIER", {})
        
        # Create or get global Loggier instance
        global _loggier_instance
        if _loggier_instance is None:
            _loggier_instance = Loggier(
                api_key=config.get("API_KEY"),
                api_url=config.get("API_URL"),
                project_name=config.get("PROJECT_NAME"),
                environment=config.get("ENVIRONMENT", "development"),
                async_mode=config.get("ASYNC_MODE", True),
                max_batch_size=config.get("MAX_BATCH_SIZE", 100),
                flush_interval=config.get("FLUSH_INTERVAL", 5),
                tags=config.get("TAGS", [])
            )
            
            # Add Django information to global context
            _loggier_instance.context.update_global({
                "framework": "django",
                "django_debug": getattr(settings, "DEBUG", False)
            })
        
        self.logger = _loggier_instance
        
        # Middleware configuration
        self.capture_request_data = config.get("CAPTURE_REQUEST_DATA", True)
        self.log_slow_requests = config.get("LOG_SLOW_REQUESTS", True)
        self.slow_request_threshold = config.get("SLOW_REQUEST_THRESHOLD", 1.0)
        
        # Status codes to track - default to server errors only if not specified
        self.statuses_to_track = set(config.get("STATUSES_TO_TRACK", [500]))
        
        # Body capturing settings
        self.capture_request_body = config.get("CAPTURE_REQUEST_BODY", False)
        self.capture_response_body = config.get("CAPTURE_RESPONSE_BODY", True)
        self.max_body_size = config.get("MAX_BODY_SIZE", 16384)  # 16KB default
        self.include_stacktrace = config.get("INCLUDE_STACKTRACE", True)
        
        # Store original request and response for tracked statuses
        self.store_transaction_context = True
    
    def __call__(self, request):
        """
        Process the request and response.
        
        Args:
            request: Django HTTP request
            
        Returns:
            Django HTTP response
        """
        # Check if this is a decorated view that should be tracked
        view_func = request.resolver_match.func if hasattr(request, 'resolver_match') else None
        is_tracked_view = view_func in _tracked_views if view_func else False
        track_options = getattr(view_func, '_loggier_track_options', {}) if is_tracked_view else {}
        
        # Generate request ID and record start time
        request_id = str(uuid.uuid4())
        request.loggier_request_id = request_id
        request.loggier_start_time = time.time()
        request.loggier_transaction_data = {"request": {}, "response": {}, "context": {}}
        
        # Update global context with request ID
        self.logger.context.update_global({"request_id": request_id})
        
        # Determine if we should log this request
        should_log_request = is_tracked_view or self.capture_request_data
        
        # Collect request data
        request_data = None
        if should_log_request:
            # Check if we should capture the request body
            capture_req_body = track_options.get('capture_request_body', self.capture_request_body)
            
            # Collect comprehensive request data
            request_data = self._collect_request_data(request, include_body=capture_req_body)
            
            # Store request data in transaction context
            request.loggier_transaction_data["request"] = request_data
            
            # Add any decorator tags
            decorator_tags = track_options.get('tags', [])
            if decorator_tags:
                self.logger.context.update_global({"endpoint_tags": decorator_tags})
                request.loggier_transaction_data["context"]["tags"] = decorator_tags
            
            # Log request start
            self.logger.info(f"Request started: {request.method} {request.path}", context=request_data)
        
        # Get response (try/except to catch exceptions)
        try:
            response = self.get_response(request)
            
            # Store the original response for later reference
            if hasattr(response, 'content'):
                # Only store if it's a regular HttpResponse with content
                try:
                    original_content = response.content
                    # Store a reference to the original content
                    request.loggier_original_response = original_content
                except Exception:
                    pass
                
        except Exception as exc:
            # Process exception
            if should_log_request:
                # Create exception context including request data
                exc_data = request_data.copy() if request_data else self._collect_request_data(request)
                
                # Get exception details including full traceback
                import traceback
                trace_info = {
                    "type": exc.__class__.__name__,
                    "message": str(exc),
                }
                
                if self.include_stacktrace:
                    trace_info["traceback"] = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
                
                exc_data["exception"] = trace_info
                
                # Store in transaction context
                request.loggier_transaction_data["context"]["exception"] = trace_info
                
                # Log exception
                self.logger.exception(
                    f"Exception during request: {request.method} {request.path}",
                    exception=exc,
                    context=exc_data
                )
            
            # Re-raise the exception
            raise
        
        # Process response if we have timing info
        if hasattr(request, "loggier_start_time"):
            # Calculate request time
            request_time = time.time() - request.loggier_start_time
            
            # Check if we should log slow requests
            is_slow = self.log_slow_requests and request_time > self.slow_request_threshold
            
            # Get view-specific statuses to track
            view_statuses = set(track_options.get('statuses', []))
            track_statuses = self.statuses_to_track.union(view_statuses)
            
            # Determine if this status code should be tracked
            status_tracked = response.status_code in track_statuses
            
            # Log if: it's slow, status tracked, or it's a tracked view
            if is_slow or status_tracked or is_tracked_view:
                # Check if we should capture the response body
                capture_resp_body = track_options.get('capture_response_body', self.capture_response_body)
                
                # Get comprehensive response data
                resp_data = self._collect_response_data(request, response, request_time, include_body=capture_resp_body)
                
                # Store in transaction context
                request.loggier_transaction_data["response"] = resp_data
                request.loggier_transaction_data["context"]["request_time"] = request_time
                
                # Add transaction context to log context
                log_context = {
                    "transaction": request.loggier_transaction_data,
                    **resp_data  # Include response data at top level for compatibility
                }
                
                # Log based on status code
                if 200 <= response.status_code < 300:
                    self.logger.info(
                        f"Request completed: {request.method} {request.path} - {response.status_code}",
                        context=log_context
                    )
                elif 300 <= response.status_code < 400:
                    self.logger.info(
                        f"Request redirected: {request.method} {request.path} - {response.status_code}",
                        context=log_context
                    )
                elif 400 <= response.status_code < 500:
                    self.logger.warning(
                        f"Client error: {request.method} {request.path} - {response.status_code}",
                        context=log_context
                    )
                else:
                    self.logger.error(
                        f"Server error: {request.method} {request.path} - {response.status_code}",
                        context=log_context
                    )
            
            # Always log slow requests regardless of status code
            if is_slow:
                self.logger.warning(
                    f"Slow request detected: {request.path} ({request_time:.2f}s)",
                    context={
                        "request_time": request_time,
                        "threshold": self.slow_request_threshold,
                        "path": request.path,
                        "method": request.method,
                        "transaction": request.loggier_transaction_data
                    }
                )
        
        return response
    
    def _collect_request_data(self, request, include_body=False):
        """
        Collect comprehensive data from the request object.
        
        Args:
            request: Django HTTP request
            include_body: Whether to include the request body
            
        Returns:
            dict: Request data dictionary
        """
        # Basic request data
        req_data = {
            "method": request.method,
            "path": request.path,
            "full_path": request.get_full_path(),
            "scheme": request.scheme if hasattr(request, 'scheme') else None,
            "remote_addr": request.META.get("REMOTE_ADDR", ""),
            "user_agent": request.META.get("HTTP_USER_AGENT", ""),
            "referer": request.META.get("HTTP_REFERER", ""),
        }
        
        # Add user info if available
        if hasattr(request, "user") and request.user.is_authenticated:
            user_data = {
                "user_id": request.user.id,
                "username": getattr(request.user, 'username', str(request.user)),
                "email": getattr(request.user, 'email', None),
            }
            req_data["user"] = user_data
        
        # Add query parameters if present
        if request.GET:
            req_data["query_params"] = self._filter_sensitive_data(dict(request.GET.items()))
        
        # Add request headers (filtered)
        headers = {}
        for key, value in request.META.items():
            if key.startswith('HTTP_') and not self._is_sensitive_field(key):
                header_name = key[5:].lower().replace('_', '-')
                headers[header_name] = value
        if headers:
            req_data["headers"] = headers
        
        # Add content type and length
        if 'CONTENT_TYPE' in request.META:
            req_data['content_type'] = request.META['CONTENT_TYPE']
        if 'CONTENT_LENGTH' in request.META:
            req_data['content_length'] = request.META['CONTENT_LENGTH']
        
        # Add POST data if appropriate (and not sensitive)
        if include_body and request.method in ['POST', 'PUT', 'PATCH']:
            # Handle different types of request bodies
            body_data = None
            
            # For regular form data
            if hasattr(request, 'POST') and request.POST:
                body_data = self._filter_sensitive_data(dict(request.POST.items()))
            
            # For JSON data
            elif request.content_type == 'application/json' and hasattr(request, 'body'):
                try:
                    json_data = json.loads(request.body.decode('utf-8'))
                    body_data = self._filter_sensitive_data(json_data)
                except Exception:
                    # If we can't parse JSON, include raw body up to max size
                    try:
                        body_data = request.body.decode('utf-8', errors='replace')[:self.max_body_size]
                    except Exception:
                        body_data = "[Unable to decode request body]"
            
            # For other body types, include raw body up to max size if needed
            elif hasattr(request, 'body') and request.body:
                try:
                    body_data = request.body.decode('utf-8', errors='replace')[:self.max_body_size]
                    if len(request.body) > self.max_body_size:
                        body_data += "... [truncated]"
                except Exception:
                    body_data = "[Binary data not shown]"
            
            if body_data is not None:
                req_data["body"] = body_data
        
        # Add view information if available
        if hasattr(request, 'resolver_match') and request.resolver_match:
            view_info = {
                "function": request.resolver_match.view_name,
                "url_name": request.resolver_match.url_name,
                "app_name": request.resolver_match.app_name,
                "namespace": request.resolver_match.namespace,
            }
            
            # Add route pattern if available
            if hasattr(request.resolver_match, 'route'):
                view_info["route"] = request.resolver_match.route
            
            # Add arguments and keyword arguments (filtered)
            if request.resolver_match.args:
                view_info["args"] = request.resolver_match.args
            
            if request.resolver_match.kwargs:
                view_info["kwargs"] = self._filter_sensitive_data(request.resolver_match.kwargs)
            
            req_data["view"] = view_info
        
        # Add files if present
        if hasattr(request, 'FILES') and request.FILES:
            files_info = {}
            for name, file_obj in request.FILES.items():
                files_info[name] = {
                    "name": file_obj.name,
                    "size": file_obj.size,
                    "content_type": file_obj.content_type,
                }
            req_data["files"] = files_info
        
        return req_data
    
    def _collect_response_data(self, request, response, request_time, include_body=False):
        """
        Collect comprehensive data from the response object.
        
        Args:
            request: Django HTTP request
            response: Django HTTP response
            request_time: Request processing time in seconds
            include_body: Whether to include the response body
            
        Returns:
            dict: Response data dictionary
        """
        # Basic response data
        resp_data = {
            "status_code": response.status_code,
            "request_time": round(request_time, 4),
            "request_method": request.method,
            "request_path": request.path,
        }
        
        # Add response reason phrase if available
        if hasattr(response, 'reason_phrase') and response.reason_phrase:
            resp_data["reason_phrase"] = response.reason_phrase
        
        # Add headers if available (non-sensitive only)
        if hasattr(response, "headers"):
            headers = {}
            for key, value in response.headers.items():
                if not self._is_sensitive_field(key):
                    headers[key.lower()] = value
            if headers:
                resp_data["headers"] = headers
        
        # Add content type if available
        resp_data["content_type"] = response.get("Content-Type", "")
        
        # Add content length if available
        if hasattr(response, "content"):
            resp_data["content_length"] = len(response.content)
        
        # Add response body for tracked statuses or if explicitly requested
        if include_body and hasattr(response, "content"):
            content_type = response.get("Content-Type", "")
            
            # Handle different content types
            if 'application/json' in content_type:
                try:
                    # Try to parse as JSON
                    body_data = json.loads(response.content.decode('utf-8'))
                    resp_data["body"] = self._filter_sensitive_data(body_data)
                except Exception:
                    # Fallback to raw content
                    resp_data["body"] = response.content.decode('utf-8', errors='replace')[:self.max_body_size]
            elif 'text/' in content_type:
                # Text content
                resp_data["body"] = response.content.decode('utf-8', errors='replace')[:self.max_body_size]
                if len(response.content) > self.max_body_size:
                    resp_data["body"] += "... [truncated]"
            elif include_body:
                # For binary content, just note the size
                resp_data["body"] = f"[Binary content, {len(response.content)} bytes]"
        
        # For error responses, try to parse Django debug info
        if response.status_code >= 400 and hasattr(response, "content"):
            try:
                content = response.content.decode('utf-8', errors='replace')
                
                # Look for Django traceback
                if 'Traceback (most recent call last)' in content:
                    # Extract traceback - simple approach, could be improved
                    start_idx = content.find('Traceback (most recent call last)')
                    if start_idx >= 0:
                        end_idx = content.find('\n\n', start_idx)
                        if end_idx >= 0:
                            traceback = content[start_idx:end_idx].strip()
                            resp_data["traceback"] = traceback
                
                # Look for exception type and value
                if 'Exception Type:' in content and 'Exception Value:' in content:
                    exc_type_start = content.find('Exception Type:') + len('Exception Type:')
                    exc_type_end = content.find('\n', exc_type_start)
                    exc_value_start = content.find('Exception Value:') + len('Exception Value:')
                    exc_value_end = content.find('\n', exc_value_start)
                    
                    if exc_type_end >= 0 and exc_value_end >= 0:
                        exc_type = content[exc_type_start:exc_type_end].strip()
                        exc_value = content[exc_value_start:exc_value_end].strip()
                        
                        resp_data["exception"] = {
                            "type": exc_type,
                            "value": exc_value
                        }
            except Exception:
                # If parsing fails, continue without the extra info
                pass
        
        return resp_data
    
    def _filter_sensitive_data(self, data):
        """
        Filter sensitive data from dictionaries.
        
        Args:
            data: Dictionary to filter
            
        Returns:
            dict: Filtered dictionary
        """
        if not isinstance(data, dict):
            return data
        
        filtered = {}
        for key, value in data.items():
            if self._is_sensitive_field(key):
                filtered[key] = "[FILTERED]"
            elif isinstance(value, dict):
                filtered[key] = self._filter_sensitive_data(value)
            else:
                filtered[key] = value
        return filtered
    
    def _is_sensitive_field(self, field_name):
        """
        Check if a field name contains sensitive information.
        
        Args:
            field_name: Field name to check
            
        Returns:
            bool: True if the field is sensitive
        """
        sensitive_keywords = [
            "password", "token", "auth", "secret", "key", "cookie", 
            "csrf", "session", "card", "credit", "cvv", "ssn", "social",
            "security", "private", "api_key", "apikey", "access_token",
            "refresh_token", "authorization"
        ]
        field_lower = str(field_name).lower()
        return any(keyword in field_lower for keyword in sensitive_keywords)


# Backward compatibility for legacy LoggierDjango class
class LoggierDjango(Loggier):
    """
    Legacy Django integration class for backward compatibility.
    For new projects, use LoggierDjangoMiddleware directly.
    """
    
    def __init__(
        self,
        config=None,
        api_key=None,
        api_url=None,
        environment="development",
        async_mode=True,
        max_queue_size=100,
        flush_interval=5,
        log_level=None,
        tags=None,
        statuses_to_track=None,
        capture_request_data=True,
        log_slow_requests=True,
        slow_request_threshold=1.0,
        capture_request_body=False,
        capture_response_body=True
    ):
        """Initialize Django integration."""
        # Get configuration from Django settings
        self.config = config or getattr(settings, "LOGGIER", {})
        
        # Override with parameters if provided
        api_key = api_key or self.config.get("API_KEY")
        api_url = api_url or self.config.get("API_URL")
        environment = environment or self.config.get("ENVIRONMENT", environment)
        tags = tags or self.config.get("TAGS", [])
        
        # Get log level
        if log_level is None:
            log_level = getattr(Loggier, "DEFAULT_LOG_LEVEL", None)
        
        # Initialize Loggier client
        super().__init__(
            api_key=api_key,
            api_url=api_url,
            environment=environment,
            async_mode=async_mode,
            max_batch_size=max_queue_size,  # renamed parameter
            flush_interval=flush_interval,
            log_level=log_level,
            tags=tags
        )
        
        # Add Django context
        self.context.update_global({
            "framework": "django",
            "django_debug": getattr(settings, "DEBUG", False)
        })
        
        # Django-specific settings
        self.capture_request_data = capture_request_data
        self.log_slow_requests = log_slow_requests
        self.slow_request_threshold = slow_request_threshold
        self.statuses_to_track = set(statuses_to_track or self.config.get("STATUSES_TO_TRACK", [500]))
        self.capture_request_body = capture_request_body
        self.capture_response_body = capture_response_body
    
    def get_middleware(self):
        """
        Get a middleware class for use in Django MIDDLEWARE setting.
        """
        logger = self
        statuses = self.statuses_to_track
        
        class LoggierLegacyMiddleware:
            def __init__(self, get_response=None):
                self.get_response = get_response
            
            def __call__(self, request):
                # Initialize transaction data
                request.loggier_request_id = str(uuid.uuid4())
                request.loggier_start_time = time.time()
                request.loggier_transaction_data = {"request": {}, "response": {}, "context": {}}
                
                # Update global context
                logger.context.update_global({"request_id": request.loggier_request_id})
                
                # Log request if enabled
                if logger.capture_request_data:
                    # Collect request data
                    req_data = self._collect_request_data(request, logger.capture_request_body)
                    request.loggier_transaction_data["request"] = req_data
                    
                    # Log request
                    logger.info(f"Request started: {request.method} {request.path}", context=req_data)
                
                # Process request
                try:
                    response = self.get_response(request)
                except Exception as exc:
                    # Collect exception data
                    exc_data = self._collect_request_data(request, logger.capture_request_body)
                    
                    # Get exception traceback
                    import traceback
                    trace_info = {
                        "type": exc.__class__.__name__,
                        "message": str(exc),
                        "traceback": "".join(traceback.format_exception(
                            type(exc), exc, exc.__traceback__
                        ))
                    }
                    exc_data["exception"] = trace_info
                    request.loggier_transaction_data["context"]["exception"] = trace_info
                    
                    # Log exception
                    logger.exception(
                        f"Exception during request: {request.method} {request.path}",
                        exception=exc,
                        context=exc_data
                    )
                    raise
                
                # Process response
                if hasattr(request, "loggier_start_time"):
                    # Calculate request time
                    request_time = time.time() - request.loggier_start_time
                    request.loggier_transaction_data["context"]["request_time"] = request_time
                    
                    # Check if we should log this response based on status
                    should_log = (
                        logger.capture_request_data and
                        (response.status_code in statuses)
                    )
                    
                    if should_log:
                        # Collect response data
                        resp_data = self._collect_response_data(
                            request, response, request_time, logger.capture_response_body
                        )
                        request.loggier_transaction_data["response"] = resp_data
                        
                        # Build complete transaction context
                        transaction_context = {
                            "transaction": request.loggier_transaction_data,
                            **resp_data  # Include response data at top level for compatibility
                        }
                        
                        # Log based on status code
                        if 200 <= response.status_code < 300:
                            logger.info(
                                f"Request completed: {request.method} {request.path} - {response.status_code}",
                                context=transaction_context
                            )
                        elif 300 <= response.status_code < 400:
                            logger.info(
                                f"Request redirected: {request.method} {request.path} - {response.status_code}",
                                context=transaction_context
                            )
                        elif 400 <= response.status_code < 500:
                            logger.warning(
                                f"Client error: {request.method} {request.path} - {response.status_code}",
                                context=transaction_context
                            )
                        else:
                            logger.error(
                                f"Server error: {request.method} {request.path} - {response.status_code}",
                                context=transaction_context
                            )
                    
                    # Always log slow requests
                    if logger.log_slow_requests and request_time > logger.slow_request_threshold:
                        logger.warning(
                            f"Slow request detected: {request.path} ({request_time:.2f}s)",
                            context={
                                "request_time": request_time,
                                "threshold": logger.slow_request_threshold,
                                "path": request.path,
                                "method": request.method,
                                "transaction": request.loggier_transaction_data
                            }
                        )
                
                return response
            
            def _collect_request_data(self, request, include_body=False):
                """Collect request data"""
                req_data = {
                    "method": request.method,
                    "path": request.path,
                    "full_path": request.get_full_path(),
                    "remote_addr": request.META.get("REMOTE_ADDR", ""),
                    "user_agent": request.META.get("HTTP_USER_AGENT", ""),
                }
                
                # Add user info
                if hasattr(request, "user") and request.user.is_authenticated:
                    req_data["user"] = {
                        "user_id": request.user.id,
                        "username": getattr(request.user, 'username', str(request.user)),
                    }
                
                # Add query params
                if request.GET:
                    req_data["query_params"] = dict(request.GET.items())
                
                # Add body if requested and available
                if include_body and request.method in ['POST', 'PUT', 'PATCH']:
                    if hasattr(request, 'POST') and request.POST:
                        req_data["body"] = dict(request.POST.items())
                    elif hasattr(request, 'body') and request.content_type == 'application/json':
                        try:
                            json_data = json.loads(request.body.decode('utf-8'))
                            req_data["body"] = json_data
                        except Exception:
                            # If we can't parse JSON, include raw body
                            try:
                                req_data["body"] = request.body.decode('utf-8', errors='replace')[:4096]
                            except Exception:
                                pass
                
                return req_data
            
            def _collect_response_data(self, request, response, request_time, include_body=False):
                """Collect response data"""
                resp_data = {
                    "status_code": response.status_code,
                    "content_type": response.get("Content-Type", ""),
                    "request_time": round(request_time, 4)
                }
                
                # Add content length if available
                if hasattr(response, "content"):
                    resp_data["content_length"] = len(response.content)
                
                # Add headers if available
                if hasattr(response, "headers"):
                    headers = {}
                    for key, value in response.headers.items():
                        headers[key.lower()] = value
                    resp_data["headers"] = headers
                
                # Add body if requested and available
                if include_body and hasattr(response, "content"):
                    content_type = response.get("Content-Type", "")
                    
                    # Handle different content types
                    if 'application/json' in content_type:
                        try:
                            # Try to parse as JSON
                            body_data = json.loads(response.content.decode('utf-8'))
                            resp_data["body"] = body_data
                        except Exception:
                            # Fallback to raw content (truncated)
                            resp_data["body"] = response.content.decode('utf-8', errors='replace')[:4096]
                    elif 'text/' in content_type:
                        # Text content (truncated)
                        resp_data["body"] = response.content.decode('utf-8', errors='replace')[:4096]
                    
                    # For error responses, try to parse Django debug info
                    if response.status_code >= 400:
                        try:
                            content = response.content.decode('utf-8', errors='replace')
                            
                            # Look for Django traceback
                            if 'Traceback (most recent call last)' in content:
                                # Extract traceback
                                start_idx = content.find('Traceback (most recent call last)')
                                if start_idx >= 0:
                                    end_idx = content.find('\n\n', start_idx)
                                    if end_idx >= 0:
                                        traceback = content[start_idx:end_idx].strip()
                                        resp_data["traceback"] = traceback
                        except Exception:
                            pass
                
                return resp_data
        
        return LoggierLegacyMiddleware