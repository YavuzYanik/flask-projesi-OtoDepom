# OtoDepom - app Klasörü (AI Context)
**Bağlam:** Bu klasör OtoDepom uygulamasının çekirdek modülüdür. Application Factory Pattern kullanılarak Flask uygulaması burada oluşturulur (`__init__.py`). Veritabanı modelleri (`models.py`) tüm blueprint'ler tarafından erişilebilir olması için bu kök klasörde bulunur.
**Kısıtlar:** `app` nesnesi doğrudan import edilmez, her zaman `current_app` veya blueprint mekanizmaları kullanılır. Modeller SQLAlchemy 2.x Mapped stiliyle yazılır.
