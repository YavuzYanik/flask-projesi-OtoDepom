# OtoDepom - app/auth Klasörü (AI Context)
**Bağlam:** Uygulamanın kimlik doğrulama (authentication) blueprint'idir.
**Görev:** Kullanıcı kayıt olma (register), giriş yapma (login) ve çıkış yapma (logout) işlemleri burada gerçekleşir. 
**Kısıtlar:** Flask-WTF ile form doğrulaması (CSRF dahil) yapılmalı, şifreler `generate_password_hash` ile şifrelenmeli ve düz metin şifre asla kabul edilmemelidir. Form sınıfları `forms.py` dosyasına yazılır.
