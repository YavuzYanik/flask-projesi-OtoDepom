# OtoDepom - tests Klasörü (AI Context)
**Bağlam:** Uygulamanın birim testleri (Unit Tests) klasörüdür.
**Görev:** Pytest kütüphanesi kullanılarak yazılacak tüm testler burada bulunur (`test_models.py`, `test_auth.py` vb.).
**Kısıtlar:** Her bir özellik geliştirildiğinde buraya en az bir birim testi eklenmelidir. Testler, gerçek veritabanını etkilememek için in-memory (bellek içi) bir SQLite test fixture'ı (`conftest.py`) üzerinden çalıştırılır.
