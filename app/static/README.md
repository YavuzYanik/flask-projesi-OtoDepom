# OtoDepom - app/static Klasörü (AI Context)
**Bağlam:** Projenin statik dosyaları (CSS, JS, Görseller) burada barındırılır.
**Görev:** Özel tasarım CSS dosyaları (`style.css`), JavaScript dosyaları veya ürün logoları gibi değişmeyen dosyalar burada klasörlenir (ör. `css/`, `img/`, `js/`).
**Kısıtlar:** Frontend framework'leri haricinde yazılacak tüm vanilla CSS'ler buraya eklenmeli ve şablonlarda `url_for('static', filename='...')` ile çağrılmalıdır.
