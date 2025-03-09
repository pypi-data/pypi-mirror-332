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

```python
# Flask entegrasyonu
from loggier.integrations.flask import LoggierFlask

app = Flask(__name__)
logger = LoggierFlask(app, api_key="your_api_key_here")

# Django entegrasyonu
from loggier.integrations.django import LoggierDjango

LOGGIER = {
    'API_KEY': 'your_api_key_here',
    'ENVIRONMENT': 'production',
}

logger = LoggierDjango(LOGGIER)
```

### Özel Yapılandırma

```python
logger = LOGGIER(
    api_key="your_api_key_here",
    host="https://your-custom-host.com/api/ingest",
    environment="production",
    tags=["backend", "payment-service"],
    async_mode=True,
    max_queue_size=1000,
    flush_interval=10,  # saniye cinsinden
    context={"app_version": "1.0.0"}
)
```

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir issue açın veya pull request gönderin.

## Lisans

MIT Lisansı altında dağıtılmaktadır.
