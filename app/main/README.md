# OtoDepom - app/main Klasörü (AI Context)
**Bağlam:** Uygulamanın ana (main) blueprint'idir.
**Görev:** Kullanıcıların göreceği ana sayfa, ürün (Yağ, Akü, Lastik) listeleme, araca göre filtreleme (uyumluluk kontrolü) ve sipariş ekranları gibi genel rotalar (routes) burada yer alır.
**Kısıtlar:** Kimlik doğrulama gerektiren rotalarda `@login_required` dekoratörü kullanılmalıdır. Bütün şablonlar `app/templates/main` altından çağrılır.
