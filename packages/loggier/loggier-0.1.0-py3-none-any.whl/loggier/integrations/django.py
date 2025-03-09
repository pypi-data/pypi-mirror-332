import time
import traceback
from typing import Any, Dict, Optional, List, Union
import uuid

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from ..client import Loggier

class LoggierDjango(Loggier):
    """
    Django uygulamaları için Loggier entegrasyonu
    """
    
    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        api_key: Optional[str] = None,
        api_url: str = "https://api.loggier.com/api/ingest",  # host -> api_url olarak değiştirildi
        environment: str = "development",
        async_mode: bool = True,
        max_queue_size: int = 100,
        flush_interval: int = 5,
        log_level: str = 'info',
        tags: Optional[List[str]] = None,
        context: Optional[Dict[str, Any]] = None,
        capture_request_data: bool = True,
        log_slow_requests: bool = True,
        slow_request_threshold: float = 1.0  # saniye cinsinden
    ):
        """
        Django entegrasyonunu başlat
        
        Args:
            config (Dict[str, Any], optional): settings.py'dan yapılandırma
            api_key (str, optional): Loggier API anahtarı (config'den de alınabilir)
            api_url (str, optional): API endpoint URL'i (host -> api_url olarak değiştirildi)
            environment (str, optional): Ortam adı
            async_mode (bool, optional): Asenkron log gönderimi yapılsın mı?
            max_queue_size (int, optional): Asenkron modda maksimum kuyruk boyutu
            flush_interval (int, optional): Asenkron modda otomatik gönderim aralığı (saniye)
            tags (List[str], optional): Tüm loglara eklenecek etiketler
            context (Dict[str, Any], optional): Global bağlam bilgileri
            min_level (str, optional): Minimum log seviyesi
            capture_request_data (bool, optional): HTTP istek verilerini yakala
            log_slow_requests (bool, optional): Yavaş istekleri logla
            slow_request_threshold (float, optional): Yavaş istek eşiği (saniye)
        """
        # Django yapılandırmasından ayarları al
        self.config = config or getattr(settings, "LOGGIER", {})
        
        api_key = api_key or self.config.get("API_KEY")
        environment = environment or self.config.get("ENVIRONMENT", environment)
        tags = tags or self.config.get("TAGS", [])
        context = context or self.config.get("CONTEXT", {})
        
        # Django ortam bilgilerini ekle
        context = context or {}
        if hasattr(settings, "DEBUG"):
            context["django_debug"] = settings.DEBUG
        
        # Ana Loggier sınıfını başlat
        super().__init__(
            api_key=api_key,
            api_url=api_url,  # host -> api_url olarak değiştirildi
            environment=environment,
            async_mode=async_mode,
            max_batch_size=max_queue_size,  # max_queue_size -> max_batch_size olarak değiştirildi
            flush_interval=flush_interval,
            tags=tags,
            context=context,
            log_level=log_level
            # min_level kaldırıldı, Loggier sınıfında bu parametre olmayabilir
        )
        
        # Django özellikleri
        self.capture_request_data = capture_request_data or self.config.get("CAPTURE_REQUEST_DATA", True)
        self.log_slow_requests = log_slow_requests or self.config.get("LOG_SLOW_REQUESTS", True)
        self.slow_request_threshold = slow_request_threshold or self.config.get("SLOW_REQUEST_THRESHOLD", 1.0)
    
    def get_middleware(self):
        """
        Django middleware'i al
        
        Returns:
            MiddlewareMixin: Django middleware sınıfı
        """
        logger = self
        
        class LoggierMiddleware(MiddlewareMixin):
            def process_request(self, request):
                """
                İstek geldiğinde çalışır
                """
                # İstek ID'si oluştur
                request.loggier_request_id = str(uuid.uuid4())
                request.loggier_start_time = time.time()
                
                # İstek bağlamını ekle
                if logger.capture_request_data:
                    with logger.context(request_id=request.loggier_request_id):
                        logger._capture_request_start(request)
                
                return None
            
            def process_response(self, request, response):
                """
                Yanıt döndürülmeden önce çalışır
                """
                if hasattr(request, "loggier_start_time"):
                    # İstek süresini hesapla
                    request_time = time.time() - request.loggier_start_time
                    
                    # İstek bağlamı
                    if hasattr(request, "loggier_request_id") and logger.capture_request_data:
                        with logger.context(request_id=request.loggier_request_id):
                            logger._capture_request_end(request, response, request_time)
                    
                    # Yavaş istek kontrolü
                    if logger.log_slow_requests and request_time > logger.slow_request_threshold:
                        with logger.context(request_id=getattr(request, "loggier_request_id", None)):
                            logger.warning(
                                f"Yavaş istek tespit edildi: {request.path} ({request_time:.2f}s)",
                                context={  # extra -> context olarak değiştirildi
                                    "request_time": request_time,
                                    "threshold": logger.slow_request_threshold,
                                    "path": request.path,
                                    "method": request.method
                                }
                            )
                
                return response
            
            def process_exception(self, request, exception):
                """
                İstek işlenirken hata oluştuğunda çalışır
                """
                if hasattr(request, "loggier_request_id") and logger.capture_request_data:
                    with logger.context(request_id=request.loggier_request_id):
                        logger._capture_exception(request, exception)
                
                return None
        
        return LoggierMiddleware
    
    def _capture_request_start(self, request: HttpRequest) -> None:
        """
        İstek başlangıcını yakala
        
        Args:
            request (HttpRequest): Django istek nesnesi
        """
        # İstek bilgilerini topla
        req_data = {
            "method": request.method,
            "path": request.path,
            "remote_addr": request.META.get("REMOTE_ADDR"),
            "user_agent": request.META.get("HTTP_USER_AGENT"),
        }
        
        # Kullanıcı bilgisi
        if hasattr(request, "user") and request.user.is_authenticated:
            req_data["user_id"] = request.user.id
            req_data["username"] = request.user.username
        
        # Hassas bilgileri filtreleyerek query parametrelerini al
        if request.GET:
            filtered_args = {}
            for key, value in request.GET.items():
                if not self._is_sensitive_data(key):
                    filtered_args[key] = value
            req_data["query_params"] = filtered_args
        
        self.info(f"İstek başladı: {request.method} {request.path}", context=req_data)  # extra -> context olarak değiştirildi
    
    def _capture_request_end(self, request: HttpRequest, response: HttpResponse, request_time: float) -> None:
        """
        İstek sonucunu yakala
        
        Args:
            request (HttpRequest): Django istek nesnesi
            response (HttpResponse): Django yanıt nesnesi
            request_time (float): İstek süresi (saniye)
        """
        # Yanıt bilgilerini topla
        resp_data = {
            "status_code": response.status_code,
            "content_type": response.get('Content-Type', ''),
            "content_length": len(response.content) if hasattr(response, 'content') else 0,
            "request_time": round(request_time, 4)
        }
        
        # Başarılı yanıtlar
        if 200 <= response.status_code < 400:
            self.info(
                f"İstek tamamlandı: {request.method} {request.path} - {response.status_code}",
                context=resp_data  # extra -> context olarak değiştirildi
            )
        # Yönlendirmeler
        elif 300 <= response.status_code < 400:
            self.info(
                f"İstek yönlendirildi: {request.method} {request.path} - {response.status_code}",
                context=resp_data  # extra -> context olarak değiştirildi
            )
        # İstemci hataları
        elif 400 <= response.status_code < 500:
            self.warning(
                f"İstemci hatası: {request.method} {request.path} - {response.status_code}",
                context=resp_data  # extra -> context olarak değiştirildi
            )
        # Sunucu hataları
        else:
            self.error(
                f"Sunucu hatası: {request.method} {request.path} - {response.status_code}",
                context=resp_data  # extra -> context olarak değiştirildi
            )
    
    def _capture_exception(self, request: HttpRequest, exception: Exception) -> None:
        """
        İstek sırasında oluşan hatayı yakala
        
        Args:
            request (HttpRequest): Django istek nesnesi
            exception (Exception): Yakalanan hata
        """
        # İstek bilgilerini topla
        req_data = {
            "method": request.method,
            "path": request.path,
            "remote_addr": request.META.get("REMOTE_ADDR"),
            "user_agent": request.META.get("HTTP_USER_AGENT"),
        }
        
        # Kullanıcı bilgisi
        if hasattr(request, "user") and request.user.is_authenticated:
            req_data["user_id"] = request.user.id
            req_data["username"] = request.user.username
        
        # Hatayı logla
        self.exception(
            f"İstek işlenirken hata oluştu: {request.method} {request.path}",
            exception=exception,  # exc_info -> exception olarak değiştirildi
            context=req_data  # extra -> context olarak değiştirildi
        )
    
    def _is_sensitive_data(self, key: str) -> bool:
        """
        Hassas veri kontrolü
        
        Args:
            key (str): Kontrol edilecek anahtar
        
        Returns:
            bool: Hassas veri ise True
        """
        sensitive_fields = [
            "password", "token", "auth", "secret", "key", "cookie", 
            "csrf", "session", "card", "credit", "cvv", "ssn", "social"
        ]
        key_lower = key.lower()
        return any(sensitive in key_lower for sensitive in sensitive_fields)