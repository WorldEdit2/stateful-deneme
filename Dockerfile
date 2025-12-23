# Python 3.9 kullan
FROM python:3.9-slim

# Çalışma klasörünü ayarla
WORKDIR /app

# Gerekli kütüphaneyi kur
RUN pip install flask

# Kodumuzu içeri kopyala
COPY app.py .

# Verilerin tutulacağı klasörü oluştur
RUN mkdir /data

# Uygulamayı başlat
CMD ["python", "app.py"]
