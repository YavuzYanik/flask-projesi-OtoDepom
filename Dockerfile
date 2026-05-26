FROM python:3.12-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Çevresel değişkenleri ayarla (Python önbelleğini kapat ve logları anında göster)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Postgresql bağlantıları için gerekli sistem bağımlılıklarını kur
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın kalanını kopyala
COPY . /app/

# Gunicorn ile production modunda başlat
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "run:app"]
