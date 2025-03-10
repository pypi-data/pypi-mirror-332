# Loggier

Loggier, Python tabanlı backend uygulamaları için geliştirilen, düşük maliyetli bir log yönetim sistemidir. Bu kütüphane, hataları ve logları yakalayıp işleyerek merkezi bir sunucuya göndermeyi sağlar.

## Kurulum

```bash
pip install loggier
```

## Hızlı Başlangıç

```python
from loggier import Loggier

# Loggier'ı başlat
logger = Loggier(api_key="your_api_key_here")

# Temel log kayıtları
logger.info("Bu bir bilgi mesajıdır")
logger.warning("Bu bir uyarı mesajıdır")
logger.error("Bu bir hata mesajıdır")

# Bağlam ile log
logger.info("Kullanıcı oturum açtı", context={"user_id": 123, "username": "testuser"})

# Hata takibi
try:
    1 / 0
except Exception as e:
    logger.exception("Bir hata oluştu", exception=e)

# Context manager kullanımı
with logger.context(transaction="ödeme işlemi", user_id=123):
    # Bu blok içindeki tüm loglara bağlam bilgisi eklenir
    logger.info("Ödeme işlemi başlatıldı")
    logger.info("Ödeme işlemi tamamlandı")
```

## Özellikler

- **Esnek Log Seviyeleri**: info, warning, error, critical
- **Asenkron Gönderim**: Uygulamanızı yavaşlatmadan log gönderimi
- **Otomatik Bağlam Toplama**: Çalışma zamanı bilgileri ve ortam verileri
- **Hata İzleme**: Otomatik istisna ve izleme yakalama
- **Özel Etiketler ve Metadata**: Loglarınızı özelleştirme
- **Otomatik Yeniden Deneme**: Bağlantı sorunlarında güvenilir log gönderimi
- **Web Framework Entegrasyonları**: Django, Flask, FastAPI için hazır entegrasyonlar

## Gelişmiş Kullanım

### Web Framework Entegrasyonları

# Django Integration Guide for Loggier

This guide explains how to integrate Loggier with your Django project for request/response logging and error tracking.

## Installation

First, ensure you have installed the Loggier package:

```bash
pip install loggier
```

## Integration Options

### Option 1: Direct Middleware (Recommended)

The simplest way to integrate Loggier with your Django project is to add `LoggierDjangoMiddleware` directly to your `MIDDLEWARE` setting in `settings.py`:

```python
# settings.py
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # If you use corsheaders
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... other middleware
    'loggier.integrations.django.LoggierDjangoMiddleware',  # Add Loggier middleware
    # ... other middleware
]

# Configure Loggier
LOGGIER = {
    'API_KEY': 'your-api-key-here',
    'API_URL': 'http://localhost:8000/',  # Or your Loggier server URL
    'ENVIRONMENT': 'development',  # or 'production', 'staging', etc.
    'TAGS': ['django', 'web'],
    'CONTEXT': {
        'application': 'your-app-name'
    },
    'CAPTURE_REQUEST_DATA': True,
    'LOG_SLOW_REQUESTS': True,
    'SLOW_REQUEST_THRESHOLD': 1.0  # in seconds
}
```

### Option 2: Custom Middleware Module (Legacy Approach)

If you need more control over the middleware initialization, you can create a custom middleware module:

```python
# myapp/middleware.py
from loggier.integrations.django import LoggierDjango

# Create instance
loggier_django = LoggierDjango(
    api_url='http://localhost:8000/',
    api_key='your-api-key-here',
    environment='development',
    tags=['django', 'web'],
    # Other parameters...
)

# Get the middleware class
LoggierMiddleware = loggier_django.get_middleware()
```

Then in your `settings.py`:

```python
MIDDLEWARE = [
    # ... other middleware
    'myapp.middleware.LoggierMiddleware',
    # ... other middleware
]
```

## Configuration Options

The `LOGGIER` settings dictionary supports the following options:

| Option                   | Description                                   | Default                              |
| ------------------------ | --------------------------------------------- | ------------------------------------ |
| `API_KEY`                | Your Loggier API key                          | Required                             |
| `API_URL`                | Loggier API endpoint                          | `https://api.loggier.com/api/ingest` |
| `ENVIRONMENT`            | Environment name (production, staging, etc.)  | `development`                        |
| `ASYNC_MODE`             | Whether to send logs asynchronously           | `True`                               |
| `MAX_BATCH_SIZE`         | Maximum batch size for async mode             | `100`                                |
| `FLUSH_INTERVAL`         | Flush interval in seconds for async mode      | `5`                                  |
| `TAGS`                   | List of tags to add to all logs               | `[]`                                 |
| `CONTEXT`                | Dictionary of context data to add to all logs | `{}`                                 |
| `LOG_LEVEL`              | Minimum log level to send                     | `info`                               |
| `CAPTURE_REQUEST_DATA`   | Whether to capture request data               | `True`                               |
| `LOG_SLOW_REQUESTS`      | Whether to log slow requests                  | `True`                               |
| `SLOW_REQUEST_THRESHOLD` | Threshold for slow requests in seconds        | `1.0`                                |

## What Gets Logged

With the default configuration, Loggier will automatically log:

1. **Request Start**: Basic information about each incoming request
2. **Request End**: Response status, timing, and size
3. **Exceptions**: Detailed exception information with traceback
4. **Slow Requests**: Warning logs for requests that exceed the threshold

## Manual Logging

You can also use the Loggier client directly in your views:

```python
from loggier import Loggier

logger = Loggier(
    api_key='your-api-key',
    api_url='http://localhost:8000/',
    environment='development'
)

def my_view(request):
    # Log information
    logger.info("Processing user data", context={"user_id": request.user.id})

    try:
        # Your code here
        result = process_data()
        logger.info("Data processed successfully", context={"result_size": len(result)})
    except Exception as e:
        # Log exceptions
        logger.exception("Error processing data", exception=e)
        raise

    return HttpResponse("Success")
```

## Troubleshooting

### Parameter Errors

If you encounter errors like `TypeError: __init__() got an unexpected keyword argument 'context'`, it means your installed version of Loggier doesn't match the expected API. Check your installed version with:

```bash
pip show loggier
```

And either:

1. Update to the latest version: `pip install --upgrade loggier`
2. Modify your middleware to match the API of your installed version

### Middleware Import Errors

Make sure the middleware path in your `MIDDLEWARE` setting exactly matches where you've defined the middleware class. If using the legacy approach, ensure you're referencing `LoggierMiddleware` (not `LoggierDjango`):

```python
# CORRECT:
'myapp.middleware.LoggierMiddleware',  # Notice it's LoggierMiddleware, not LoggierDjango

# INCORRECT:
'myapp.middleware.LoggierDjango',  # This won't work
```

### Performance Considerations

- Loggier uses asynchronous logging by default, which minimizes performance impact
- For high-traffic applications, consider adjusting the `MAX_BATCH_SIZE` and `FLUSH_INTERVAL`
- In production environments, make sure to call `flush()` during application shutdown to ensure all logs are sent
