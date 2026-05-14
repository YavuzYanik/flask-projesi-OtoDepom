# OtoDepom

## Projenin Amacı
OtoDepom, araç sahiplerinin kendi marka ve modellerine tam olarak uyan motor yağı ve lastikleri kolayca filtreleyip satın alabilmesini sağlayan bir platformdur. Bu proje, kullanıcıların araçları için doğru yedek parçayı bulma karmaşasını ortadan kaldırmayı ve güvenli bir e-ticaret deneyimi sunmayı hedeflemektedir.

## Kullanılan Teknolojiler
- **Backend:** Python, Flask 3.x, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF
- **Frontend:** Jinja2 Şablon Motoru, HTML/CSS (Gelecek aşamalarda Bootstrap veya Tailwind eklenecek)
- **Veritabanı:** SQLite (Geliştirme aşaması için)

## Kurulum Adımları
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayın:

1. **Sanal Ortamı Oluşturun ve Aktifleştirin:**
   ```bash
   python -m venv venv
   # Windows için:
   venv\Scripts\activate
   # macOS/Linux için:
   # source venv/bin/activate
   ```

2. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Çevre Değişkenlerini (Environment Variables) Ayarlayın:**
   Proje kök dizinindeki `.env.example` dosyasının bir kopyasını oluşturup adını `.env` yapın. İçerisindeki `SECRET_KEY` gibi bilgileri güncelleyin.

4. **Veritabanını Başlatın:**
   ```bash
   flask db init
   flask db migrate -m "İlk kurulum"
   flask db upgrade
   ```

## Geliştirme Komutları

- Uygulamayı geliştirme modunda çalıştırmak için:
  ```bash
  flask run
  ```
- Modellerde (veritabanı şemasında) yapılan değişiklikleri uygulamak için:
  ```bash
  flask db migrate -m "Degisiklik aciklamasi"
  flask db upgrade
  ```
- (İleride eklenecek) Testleri çalıştırmak için:
  ```bash
  pytest
  ```