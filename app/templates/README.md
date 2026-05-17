# OtoDepom - app/templates Klasörü (AI Context)
**Bağlam:** Projenin HTML şablon dosyaları (Jinja2) burada tutulur.
**Görev:** Base template (örneğin `base.html`) burada durur. Auth sayfaları `auth/`, ana sayfalar `main/` gibi alt klasörlerde organize edilir.
**Kısıtlar:** Şablon kalıtımı (Template Inheritance) kullanılmalıdır. Formlarda CSRF token'ları `{{ form.hidden_tag() }}` ile dahil edilmelidir. Tasarımda mobil uyumluluk ve modern görünüm (Bootstrap/Tailwind) hedeflenir.
