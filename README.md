## 📺 Proje Demo Videosu

**YouTube Linki:** https://youtu.be/iE0GLPCBNcI

# OTODEPOM

## Projenin Amacı
OTODEPOM, araç sahiplerinin kendi marka ve modellerine tam olarak uyan motor yağı, akü ve lastik gibi yedek parçaları kolayca filtreleyip satın alabilmesini sağlayan bir e-ticaret platformudur. Kullanıcıların "Aracıma hangi yağ çeşidi, akü voltajı veya lastik ebatı uyar?" karmaşasını ortadan kaldırır. Platform sayesinde araç tipinizi sisteme girerek aracınıza en uygun ürünleri tek tıkla görebilir ve güvenle sipariş edebilirsiniz.

## Kullanılan Teknolojiler
- **Backend:** Python, Flask 3.x, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF
- **Frontend:** Jinja2 Şablon Motoru, HTML/CSS (Bootstrap veya Tailwind entegre edilecek)
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
.
