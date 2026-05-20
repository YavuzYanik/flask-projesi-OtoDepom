import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from app import create_app, db
from app.models import User, Product, Vehicle

app = create_app()
with app.app_context():
    # Admin kullanıcısını ekle veya güncelle
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@otodepom.com',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        print("Admin user created (admin / admin123)")
    else:
        admin.is_admin = True
        print("Admin user already exists, updated role.")

    # Mevcut ürünleri temizle ve varsayılan 90+ ürünü ekle
    from app.models import product_compatibility
    db.session.execute(product_compatibility.delete())
    db.session.query(Product).delete()
    
    default_products = [
        # ==========================================
        # 30 MOTOR YAĞI
        # ==========================================        # Motor Yağları (updated with litre info and placeholder images)
        {   # Castrol EDGE LL
            'name': 'Castrol EDGE LL',
            'category': 'Motor Yağı',
            'specs': '5W-30 (5L)',
            'price': 1250.00,
            'image_url': 'https://via.placeholder.com/300?text=Castrol+EDGE+LL'
        },
        {   # Castrol Magnatec
            'name': 'Castrol Magnatec',
            'category': 'Motor Yağı',
            'specs': '5W-40 (5L)',
            'price': 1050.00,
            'image_url': 'https://via.placeholder.com/300?text=Castrol+Magnatec'
        },
        {   # Castrol GTX
            'category': 'Motor Yağı',
            'name': 'Castrol GTX',
            'specs': '20W-50 (5L)',
            'price': 650.00,
            'image_url': 'https://via.placeholder.com/300?text=Castrol+GTX'
        },
        {   # Castrol EDGE 0W-30
            'name': 'Castrol EDGE 0W-30',
            'category': 'Motor Yağı',
            'specs': '0W-30 (5L)',
            'price': 1450.00,
            'image_url': 'https://via.placeholder.com/300?text=Castrol+EDGE+0W-30'
        },
        {
            'name': 'Motul 8100 X-Clean EFE 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 C2/C3 Onaylı Tam Sentetik',
            'price': 1650.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Motul 8100 X-Cess 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Yüksek Performanslı Sentetik',
            'price': 1350.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Motul 6100 Synergie+ 10W-40',
            'category': 'Motor Yağı',
            'specs': '10W-40 Yarı Sentetik',
            'price': 950.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Motul Specific 0W-30',
            'category': 'Motor Yağı',
            'specs': '0W-30 Yakıt Ekonomisi Sağlayan Sentetik',
            'price': 1750.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Mobil 1 ESP 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Emisyon Sistemi Korumalı Sentetik',
            'price': 1490.00,
            'image_url': 'mobil1.jpg'
        },
        {
            'name': 'Mobil Super 3000 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Tam Sentetik Premium Ürün',
            'price': 1190.00,
            'image_url': 'mobil1.jpg'
        },
        {
            'name': 'Mobil Super 2000 10W-40',
            'category': 'Motor Yağı',
            'specs': '10W-40 Günlük Kullanım İçin Sentetik',
            'price': 850.00,
            'image_url': 'mobil1.jpg'
        },
        {
            'name': 'Mobil 1 FS 0W-30',
            'category': 'Motor Yağı',
            'specs': '0W-30 Gelişmiş Koruma Sağlayan Sentetik',
            'price': 1590.00,
            'image_url': 'mobil1.jpg'
        },
        {
            'name': 'Liqui Moly Top Tec 4200 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Aşınma Karşıtı Tam Sentetik',
            'price': 2100.00,
            'image_url': 'liqui-moly.webp'
        },
        {
            'name': 'Liqui Moly Leichtlauf High Tech 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Yüksek Teknolojili Sentetik',
            'price': 1850.00,
            'image_url': 'liqui-moly.webp'
        },
        {
            'name': 'Liqui Moly MoS2 Leichtlauf 10W-40',
            'category': 'Motor Yağı',
            'specs': '10W-40 Özel Katkılı Motor Yağı',
            'price': 1250.00,
            'image_url': 'liqui-moly.webp'
        },
        {
            'name': 'Liqui Moly Special Tec F 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Ford Motorları İçin Özel Sentetik',
            'price': 1950.00,
            'image_url': 'liqui-moly.webp'
        },
        {
            'name': 'Shell Helix Ultra 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Doğal Gazdan Üretilmiş Saf Sentetik',
            'price': 1390.00,
            'image_url': 'shell.webp'
        },
        {
            'name': 'Shell Helix HX8 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Dinamik Koruma Sentetik',
            'price': 1100.00,
            'image_url': 'shell.webp'
        },
        {
            'name': 'Shell Helix HX7 10W-40',
            'category': 'Motor Yağı',
            'specs': '10W-40 Tortu Önleyici Yarı Sentetik',
            'price': 890.00,
            'image_url': 'shell.webp'
        },
        {
            'name': 'Shell Helix Ultra 0W-30',
            'category': 'Motor Yağı',
            'specs': '0W-30 Düşük Sürtünmeli Sentetik',
            'price': 1550.00,
            'image_url': 'shell.webp'
        },
        {
            'name': 'Petronas Syntium 5000 XS 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Serin Zincir Teknolojili Sentetik',
            'price': 1200.00,
            'image_url': 'petronas.png'
        },
        {
            'name': 'Petronas Syntium 3000 AV 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Isı Kontrolü Yüksek Sentetik',
            'price': 1000.00,
            'image_url': 'petronas.png'
        },
        {
            'name': 'Total Quartz 9000 5W-40',
            'category': 'Motor Yağı',
            'specs': '5W-40 Aktif Temizleyici Sentetik',
            'price': 1050.00,
            'image_url': 'total.webp'
        },
        {
            'name': 'Total Quartz INEO MC3 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 DPF ve SCR Uyumlu Sentetik',
            'price': 1250.00,
            'image_url': 'total.webp'
        },
        {
            'name': 'Elf Evolution 700 Turbo D 10W-40',
            'category': 'Motor Yağı',
            'specs': '10W-40 Eski Nesil Motorlar İçin Sentetik',
            'price': 800.00,
            'image_url': 'elf.png'
        },
        {
            'name': 'BP Visco 5000 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Temiz Motor Teknolojili Sentetik',
            'price': 1150.00,
            'image_url': 'bp.png'
        },
        {
            'name': 'Opet Fullmax 5W-30',
            'category': 'Motor Yağı',
            'specs': '5W-30 Yerli Üretim Tam Sentetik',
            'price': 1050.00,
            'image_url': 'opet.png'
        },
        {
            'name': 'Castrol Magnatec Professional 5W-20',
            'category': 'Motor Yağı',
            'specs': '5W-20 Ford EcoBoost Uyumlu Sentetik',
            'price': 1400.00,
            'image_url': 'castrol.avif'
        },
        {
            'name': 'Motul Hybrid 0W-20',
            'category': 'Motor Yağı',
            'specs': '0W-20 Hibrit Araçlara Özel Tam Sentetik',
            'price': 1800.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Mobil 1 Advanced Fuel Economy 0W-20',
            'category': 'Motor Yağı',
            'specs': '0W-20 Yakıt Tasarruflu Tam Sentetik',
            'price': 1700.00,
            'image_url': 'mobil1.jpg'
        },

        # ==========================================
        # 30 LASTİK
        # ==========================================
        {
            'name': 'Michelin Primacy 4+',
            'category': 'Lastik',
            'specs': '205/55 R16 91V Yaz Lastiği',
            'price': 3450.00,
            'image_url': 'michelin.avif'
        },
        {
            'name': 'Michelin Pilot Sport 5',
            'category': 'Lastik',
            'specs': '225/45 R17 94Y Performans Yaz Lastiği',
            'price': 4850.00,
            'image_url': 'michelin.avif'
        },
        {
            'name': 'Michelin Energy Saver+',
            'category': 'Lastik',
            'specs': '185/65 R15 88T Çevre Dostu Yaz Lastiği',
            'price': 2750.00,
            'image_url': 'michelin.avif'
        },
        {
            'name': 'Continental EcoContact 6',
            'category': 'Lastik',
            'specs': '195/55 R16 87H Konfor Yaz Lastiği',
            'price': 2950.00,
            'image_url': 'continental.avif'
        },
        {
            'name': 'Continental PremiumContact 6',
            'category': 'Lastik',
            'specs': '195/60 R16 89H Premium Yaz Lastiği',
            'price': 3150.00,
            'image_url': 'continental.avif'
        },
        {
            'name': 'Continental UltraContact',
            'category': 'Lastik',
            'specs': '175/70 R13 82T Güvenli Yaz Lastiği',
            'price': 1850.00,
            'image_url': 'continental.avif'
        },
        {
            'name': 'Continental PremiumContact 7',
            'category': 'Lastik',
            'specs': '205/60 R16 96V Islak Zemin Performanslı',
            'price': 3650.00,
            'image_url': 'continental.avif'
        },
        {
            'name': 'Goodyear Eagle Sport',
            'category': 'Lastik',
            'specs': '215/60 R17 96H Spor Yaz Lastiği',
            'price': 4100.00,
            'image_url': 'goodyear.avif'
        },
        {
            'name': 'Goodyear EfficientGrip Performance 2',
            'category': 'Lastik',
            'specs': '195/65 R15 91H Uzun Ömürlü Yaz Lastiği',
            'price': 2400.00,
            'image_url': 'goodyear.avif'
        },
        {
            'name': 'Goodyear EfficientGrip Cargo 2',
            'category': 'Lastik',
            'specs': '215/75 R16 113R Hafif Ticari Lastik',
            'price': 4950.00,
            'image_url': 'goodyear.avif'
        },
        {
            'name': 'Lassa Snoways 4',
            'category': 'Lastik',
            'specs': '225/45 R17 94V XL Kış Lastiği',
            'price': 2850.00,
            'image_url': 'lassa.avif'
        },
        {
            'name': 'Lassa Greenways',
            'category': 'Lastik',
            'specs': '175/65 R14 82T Yakıt Tasarruflu',
            'price': 1650.00,
            'image_url': 'lassa.avif'
        },
        {
            'name': 'Lassa Competus H/P',
            'category': 'Lastik',
            'specs': '225/60 R17 99V SUV Yaz Lastiği',
            'price': 3900.00,
            'image_url': 'lassa.avif'
        },
        {
            'name': 'Lassa Wintus 2',
            'category': 'Lastik',
            'specs': '235/65 R16 115R Hafif Ticari Kış Lastiği',
            'price': 4500.00,
            'image_url': 'lassa.avif'
        },
        {
            'name': 'Pirelli Cinturato P7',
            'category': 'Lastik',
            'specs': '205/55 R16 91W Premium Konfor',
            'price': 3100.00,
            'image_url': 'pirelli.avif'
        },
        {
            'name': 'Pirelli P Zero',
            'category': 'Lastik',
            'specs': '245/45 R18 100Y Spor Performans',
            'price': 5800.00,
            'image_url': 'pirelli.avif'
        },
        {
            'name': 'Pirelli Scorpion Verde',
            'category': 'Lastik',
            'specs': '225/55 R18 98V SUV Çevre Dostu',
            'price': 4900.00,
            'image_url': 'pirelli.avif'
        },
        {
            'name': 'Bridgestone Turanza T005',
            'category': 'Lastik',
            'specs': '205/55 R16 91V Yüksek Islak Zemin Yol Tutuşu',
            'price': 3250.00,
            'image_url': 'bridgestone.webp'
        },
        {
            'name': 'Bridgestone Ecopia EP150',
            'category': 'Lastik',
            'specs': '175/65 R15 84H Eko Performans',
            'price': 2150.00,
            'image_url': 'bridgestone.webp'
        },
        {
            'name': 'Bridgestone Alenza 001',
            'category': 'Lastik',
            'specs': '225/65 R17 102H SUV Premium',
            'price': 4400.00,
            'image_url': 'bridgestone.webp'
        },
        {
            'name': 'Hankook Ventus Prime 4',
            'category': 'Lastik',
            'specs': '215/50 R17 95W Gelişmiş Emniyet',
            'price': 3700.00,
            'image_url': 'hankook.png'
        },
        {
            'name': 'Hankook Kinergy Eco 2',
            'category': 'Lastik',
            'specs': '185/55 R16 83V Ekonomik Yaz Lastiği',
            'price': 2650.00,
            'image_url': 'hankook.png'
        },
        {
            'name': 'Hankook Dynapro HP2',
            'category': 'Lastik',
            'specs': '225/60 R18 100H SUV Konfor',
            'price': 4600.00,
            'image_url': 'hankook.png'
        },
        {
            'name': 'Nokian Wetproof',
            'category': 'Lastik',
            'specs': '185/60 R15 88T Islak Zeminde Mükemmel Tutuş',
            'price': 2300.00,
            'image_url': 'nokian.png'
        },
        {
            'name': 'Nokian Seasonproof',
            'category': 'Lastik',
            'specs': '235/60 R18 107V Dört Mevsim SUV Lastik',
            'price': 5100.00,
            'image_url': 'nokian.png'
        },
        {
            'name': 'Michelin Primacy 4',
            'category': 'Lastik',
            'specs': '215/55 R17 94V Güvenli ve Uzun Ömürlü',
            'price': 4200.00,
            'image_url': 'michelin.avif'
        },
        {
            'name': 'Continental WinterContact TS 870',
            'category': 'Lastik',
            'specs': '215/55 R16 93H Premium Kış Lastiği',
            'price': 3800.00,
            'image_url': 'continental.avif'
        },
        {
            'name': 'Goodyear UltraGrip 9+',
            'category': 'Lastik',
            'specs': '185/60 R15 84T Güvenli Kar Performansı',
            'price': 2250.00,
            'image_url': 'goodyear.avif'
        },
        {
            'name': 'Pirelli Carrier',
            'category': 'Lastik',
            'specs': '195/60 R15 88H Hafif Ticari Yaz Lastiği',
            'price': 3100.00,
            'image_url': 'pirelli.avif'
        },
        {
            'name': 'Bridgestone Blizzak LM005',
            'category': 'Lastik',
            'specs': '215/65 R16 98H Ödüllü Kış Lastiği',
            'price': 3950.00,
            'image_url': 'bridgestone.webp'
        },

        # ==========================================
        # 30 AKÜ
        # ==========================================
        {
            'name': 'Varta D24 Blue Dynamic',
            'category': 'Akü',
            'specs': '12V 60Ah 540A Çelik Akü',
            'price': 2750.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Varta E11 Blue Dynamic',
            'category': 'Akü',
            'specs': '12V 74Ah 680A Yüksek Marş Gücü',
            'price': 3200.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Varta C22 Black Dynamic',
            'category': 'Akü',
            'specs': '12V 52Ah 470A Standart Koruma',
            'price': 2200.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Varta E39 Silver Dynamic AGM',
            'category': 'Akü',
            'specs': '12V 70Ah Start-Stop AGM Akü',
            'price': 4950.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Varta A14 Blue Dynamic',
            'category': 'Akü',
            'specs': '12V 40Ah Japon Standart Akü',
            'price': 1850.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Varta E43 Black Dynamic',
            'category': 'Akü',
            'specs': '12V 45Ah Küçük Araç Aküsü',
            'price': 2100.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Mutlu SFB M2',
            'category': 'Akü',
            'specs': '12V 60Ah Tam Kapalı SFB Teknolojisi',
            'price': 2600.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Mutlu SFB M3',
            'category': 'Akü',
            'specs': '12V 72Ah Yüksek Güç SFB Akü',
            'price': 2950.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Mutlu SFB M1',
            'category': 'Akü',
            'specs': '12V 50Ah Bakımsız Eko Akü',
            'price': 2300.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Mutlu AGM Stop-Start',
            'category': 'Akü',
            'specs': '12V 70Ah AGM Akü',
            'price': 4700.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Mutlu SFB Heavy Duty',
            'category': 'Akü',
            'specs': '12V 75Ah Hafif Ticari Aküsü',
            'price': 3200.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Mutlu SFB M2 45Ah',
            'category': 'Akü',
            'specs': '12V 45Ah Asya Tipi Dar Kutup',
            'price': 2050.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'İnci Akü Formul A Taurus',
            'category': 'Akü',
            'specs': '12V 60Ah Gelişmiş Eko Akü',
            'price': 2550.00,
            'image_url': 'inci.jpg'
        },
        {
            'name': 'İnci Akü Formul A Taurus 72Ah',
            'category': 'Akü',
            'specs': '12V 72Ah Yüksek Marş Kapasitesi',
            'price': 2850.00,
            'image_url': 'inci.jpg'
        },
        {
            'name': 'İnci Akü Formul A Taurus 50Ah',
            'category': 'Akü',
            'specs': '12V 50Ah Bakımsız Akü',
            'price': 2250.00,
            'image_url': 'inci.jpg'
        },
        {
            'name': 'İnci Akü Maxim A Gorilla',
            'category': 'Akü',
            'specs': '12V 80Ah Üstün Çevrim Ömrü',
            'price': 3700.00,
            'image_url': 'inci.jpg'
        },
        {
            'name': 'İnci Akü Formul A Taurus 45Ah',
            'category': 'Akü',
            'specs': '12V 45Ah Japon Uyumlu Dar Kutu',
            'price': 1950.00,
            'image_url': 'inci.jpg'
        },
        {
            'name': 'Bosch S4 005',
            'category': 'Akü',
            'specs': '12V 60Ah Güçlü Gümüş Alaşım',
            'price': 2800.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'Bosch S4 008',
            'category': 'Akü',
            'specs': '12V 74Ah 680A Dayanıklı Plaka',
            'price': 3300.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'Bosch S3 002',
            'category': 'Akü',
            'specs': '12V 45Ah Standart Tip',
            'price': 2000.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'Bosch S5 A08 AGM',
            'category': 'Akü',
            'specs': '12V 70Ah AGM Yüksek Donanım',
            'price': 5200.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'Bosch S4 001',
            'category': 'Akü',
            'specs': '12V 44Ah Eko Seri',
            'price': 1900.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'Yiğit Akü Prestij',
            'category': 'Akü',
            'specs': '12V 60Ah Güvenilir Yerli Akü',
            'price': 2400.00,
            'image_url': 'yigit.png'
        },
        {
            'name': 'Yiğit Akü Prestij 72Ah',
            'category': 'Akü',
            'specs': '12V 72Ah Standart Akü',
            'price': 2750.00,
            'image_url': 'yigit.png'
        },
        {
            'name': 'Yiğit Akü Prestij 50Ah',
            'category': 'Akü',
            'specs': '12V 50Ah Uzun Raf Ömrü',
            'price': 2100.00,
            'image_url': 'yigit.png'
        },
        {
            'name': 'Yiğit Akü Prestij 45Ah',
            'category': 'Akü',
            'specs': '12V 45Ah İnce Kutup Akü',
            'price': 1800.00,
            'image_url': 'yigit.png'
        },
        {
            'name': 'Yiğit Akü Heavy Duty 75Ah',
            'category': 'Akü',
            'specs': '12V 75Ah Güçlendirilmiş Plaka',
            'price': 3000.00,
            'image_url': 'yigit.png'
        },
        {
            'name': 'EAS Akü Aktiv',
            'category': 'Akü',
            'specs': '12V 60Ah Kaliteli Akü',
            'price': 2350.00,
            'image_url': 'eas.png'
        },
        {
            'name': 'President Akü Gold',
            'category': 'Akü',
            'specs': '12V 60Ah Ekonomik Alternatif',
            'price': 2250.00,
            'image_url': 'president.png'
        },
        {
            'name': 'Hugel Akü Ultra',
            'category': 'Akü',
            'specs': '12V 60Ah Uzun Ömürlü Çift Kapak',
            'price': 2300.00,
            'image_url': 'hugel.png'
        },
        
        # ==========================================
        # JANTLAR (EKSTRA)
        # ==========================================
        {
            'name': 'Vossen CV3 16"',
            'category': 'Jant',
            'specs': '16 inç 5x112 Alaşımlı Jant',
            'price': 8500.00,
            'image_url': 'jant1.jpg'
        },
        {
            'name': 'Vossen CV3 17"',
            'category': 'Jant',
            'specs': '17 inç 5x112 Alaşımlı Jant',
            'price': 9800.00,
            'image_url': 'jant1.jpg'
        },
        {
            'name': 'Vossen CV3 18"',
            'category': 'Jant',
            'specs': '18 inç 5x120 Alaşımlı Jant',
            'price': 12000.00,
            'image_url': 'jant1.jpg'
        },
        {
            'name': 'MOMO Revenge 15"',
            'category': 'Jant',
            'specs': '15 inç 4x100 Siyah Jant',
            'price': 7200.00,
            'image_url': 'jant2.jpg'
        }
    ]

    # Ürünleri ekle
    for p_data in default_products:
        p = Product(
            name=p_data['name'],
            category=p_data['category'],
            specs=p_data['specs'],
            price=p_data['price'],
            image_url=p_data['image_url']
        )
        db.session.add(p)

    db.session.commit()
    print(f"Added {len(default_products)} new products to the database.")

    # Tüm araçları tekrar uyuştur
    from app.cars_data import link_vehicle_products
    all_vehicles = Vehicle.query.all()
    print(f"Updating compatibility links for {len(all_vehicles)} vehicles in the database...")
    for v in all_vehicles:
        link_vehicle_products(v)
    db.session.commit()
    print("Database seeding and dynamic product compatibility mapping completed successfully!")
