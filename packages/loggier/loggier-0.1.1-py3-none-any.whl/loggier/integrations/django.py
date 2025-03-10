"""
Django middleware integration for Loggier.
"""
import uuid
import time
from typing import Dict, List, Any, Optional, Union, Callable

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from ..client import Loggier

# Global Loggier instance for the middleware
_loggier_instance = None

class LoggierDjangoMiddleware:
    """
    Django middleware for Loggier integration.
    
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
        'SLOW_REQUEST_THRESHOLD': 1.0  # seconds
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
                tags=config.get("TAGS", []),
                service_name=config.get("SERVICE_NAME"),
                capture_uncaught = config.get("CAPTURE_UNCAUGHT"),
                log_level=config.get("LOG_LEVEL"),
                sensitive_fields=config.get("SENSITIVE_KEYS"),
                max_retries=config.get("MAX_RETIRES"),
                http_timeout=config.get("HTTP_TIMEOUT"),
                enable_performance_monitoring=config.get("ENABLE_PERFORMANCE_MONITORING")
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
        self.statuses_to_track = config.get("STATUSES_TO_TRACK", [])
    
    def __call__(self, request):
        """
        Process the request and response.
        
        Args:
            request: Django HTTP request
            
        Returns:
            Django HTTP response
        """
        # Process request
        request_id = str(uuid.uuid4())
        request.loggier_request_id = request_id
        request.loggier_start_time = time.time()
        
        # Log request data
        if self.capture_request_data:
            # Update global context with request ID
            self.logger.context.update_global({"request_id": request_id})
            
            # Collect request data
            req_data = {
                "method": request.method,
                "path": request.path,
                "remote_addr": request.META.get("REMOTE_ADDR", ""),
                "user_agent": request.META.get("HTTP_USER_AGENT", "")
            }
            
            # Add user info if available
            if hasattr(request, "user") and request.user.is_authenticated:
                req_data["user_id"] = request.user.id
                req_data["username"] = request.user.username
            
            # Filter query parameters
            if request.GET:
                filtered_params = {}
                for key, value in request.GET.items():
                    if not self._is_sensitive_field(key):
                        filtered_params[key] = value
                if filtered_params:
                    req_data["query_params"] = filtered_params
            
            # Log request
            # self.logger.info(f"Request started: {request.method} {request.path}", context=req_data)
        
        # Process the request (get response)
        try:
            response = self.get_response(request)
        except Exception as exc:
            # Log exception
            if self.capture_request_data:
                self.logger.context.update_global({"request_id": request_id})
                
                # Collect context data
                exc_data = {
                    "method": request.method,
                    "path": request.path
                }
                
                # Log exception
                self.logger.exception(
                    f"Exception during request: {request.method} {request.path}",
                    exception=exc,
                    context=exc_data
                )
            
            # Re-raise the exception
            raise
        
        # Process response
        if hasattr(request, "loggier_start_time"):
            # Calculate request time
            request_time = time.time() - request.loggier_start_time
            
            if self.capture_request_data and response.status_code in self.statuses_to_track:
                self.logger.context.update_global({"request_id": request_id})
                
                # Collect response data
                resp_data = {
                    "status_code": response.status_code,
                    "content_type": response.get("Content-Type", ""),
                    "content_length": len(response.content) if hasattr(response, "content") else 0,
                    "request_time": round(request_time, 4)
                }
                
                # Log response based on status code
                if 200 <= response.status_code < 300:
                    self.logger.info(
                        f"Request completed: {request.method} {request.path} - {response.status_code}",
                        context=resp_data
                    )
                elif 300 <= response.status_code < 400:
                    self.logger.info(
                        f"Request redirected: {request.method} {request.path} - {response.status_code}",
                        context=resp_data
                    )
                elif 400 <= response.status_code < 500:
                    self.logger.warning(
                        f"Client error: {request.method} {request.path} - {response.status_code}",
                        context=resp_data
                    )
                else:
                    self.logger.error(
                        f"Server error: {request.method} {request.path} - {response.status_code}",
                        context=resp_data
                    )
            
            # Log slow requests
            if self.log_slow_requests and request_time > self.slow_request_threshold:
                self.logger.warning(
                    f"Slow request detected: {request.path} ({request_time:.2f}s)",
                    context={
                        "request_time": request_time,
                        "threshold": self.slow_request_threshold,
                        "path": request.path,
                        "method": request.method
                    }
                )
        
        return response
    
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
            "csrf", "session", "card", "credit", "cvv", "ssn", "social"
        ]
        field_lower = field_name.lower()
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
        log_level=Loggier.DEFAULT_LOG_LEVEL,
        tags=None,
        context=None,
        capture_request_data=True,
        log_slow_requests=True,
        slow_request_threshold=1.0
    ):
        """Initialize Django integration."""
        # Get configuration from Django settings
        self.config = config or getattr(settings, "LOGGIER", {})
        
        # Override with parameters if provided
        api_key = api_key or self.config.get("API_KEY")
        api_url = api_url or self.config.get("API_URL")
        environment = environment or self.config.get("ENVIRONMENT", environment)
        tags = tags or self.config.get("TAGS", [])
        
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
        
        if context:
            self.context.update_global(context)
        
        # Django-specific settings
        self.capture_request_data = capture_request_data
        self.log_slow_requests = log_slow_requests
        self.slow_request_threshold = slow_request_threshold
    
    def get_middleware(self):
        """
        Get a middleware class for use in Django MIDDLEWARE setting.
        
        Returns:
            class: Middleware class
        """
        logger = self
        
        class LoggierLegacyMiddleware(MiddlewareMixin):
            def process_request(self, request):
                """Process request."""
                request.loggier_request_id = str(uuid.uuid4())
                request.loggier_start_time = time.time()
                
                if logger.capture_request_data:
                    logger.context.update_global({"request_id": request.loggier_request_id})
                    
                    # Collect request data
                    req_data = {
                        "method": request.method,
                        "path": request.path,
                        "remote_addr": request.META.get("REMOTE_ADDR", ""),
                        "user_agent": request.META.get("HTTP_USER_AGENT", "")
                    }
                    
                    # Add user info
                    if hasattr(request, "user") and request.user.is_authenticated:
                        req_data["user_id"] = request.user.id
                        req_data["username"] = request.user.username
                    
                    # Log request
                    logger.info(f"Request started: {request.method} {request.path}", context=req_data)
                
                return None
            
            def process_response(self, request, response):
                """Process response."""
                if hasattr(request, "loggier_start_time"):
                    # Calculate request time
                    request_time = time.time() - request.loggier_start_time
                    
                    # Log response
                    if hasattr(request, "loggier_request_id") and logger.capture_request_data:
                        logger.context.update_global({"request_id": request.loggier_request_id})
                        
                        # Collect response data
                        resp_data = {
                            "status_code": response.status_code,
                            "content_type": response.get("Content-Type", ""),
                            "content_length": len(response.content) if hasattr(response, "content") else 0,
                            "request_time": round(request_time, 4)
                        }
                        
                        # Log based on status code
                        if 200 <= response.status_code < 300:
                            logger.info(
                                f"Request completed: {request.method} {request.path} - {response.status_code}",
                                context=resp_data
                            )
                        elif 300 <= response.status_code < 400:
                            logger.info(
                                f"Request redirected: {request.method} {request.path} - {response.status_code}",
                                context=resp_data
                            )
                        elif 400 <= response.status_code < 500:
                            logger.warning(
                                f"Client error: {request.method} {request.path} - {response.status_code}",
                                context=resp_data
                            )
                        else:
                            logger.error(
                                f"Server error: {request.method} {request.path} - {response.status_code}",
                                context=resp_data
                            )
                    
                    # Log slow requests
                    if logger.log_slow_requests and request_time > logger.slow_request_threshold:
                        logger.context.update_global({"request_id": getattr(request, "loggier_request_id", None)})
                        logger.warning(
                            f"Slow request detected: {request.path} ({request_time:.2f}s)",
                            context={
                                "request_time": request_time,
                                "threshold": logger.slow_request_threshold,
                                "path": request.path,
                                "method": request.method
                            }
                        )
                
                return response
            
            def process_exception(self, request, exception):
                """Process exception."""
                if hasattr(request, "loggier_request_id") and logger.capture_request_data:
                    logger.context.update_global({"request_id": request.loggier_request_id})
                    
                    # Collect exception data
                    exc_data = {
                        "method": request.method,
                        "path": request.path,
                        "remote_addr": request.META.get("REMOTE_ADDR", ""),
                        "user_agent": request.META.get("HTTP_USER_AGENT", "")
                    }
                    
                    # Add user info
                    if hasattr(request, "user") and request.user.is_authenticated:
                        exc_data["user_id"] = request.user.id
                        exc_data["username"] = request.user.username
                    
                    # Log exception
                    logger.exception(
                        f"Exception during request: {request.method} {request.path}",
                        exception=exception,
                        context=exc_data
                    )
                
                return None
        
        return LoggierLegacyMiddleware