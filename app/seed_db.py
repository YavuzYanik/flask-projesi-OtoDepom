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

    # Mevcut ürünleri temizle ve varsayılan 12 ürünü ekle
    # (Zaten veritabanında varsa çift olmaması için temizliyoruz)
    from app.models import product_compatibility
    db.session.execute(product_compatibility.delete())
    db.session.query(Product).delete()
    
    default_products = [
        # Motor Yağları
        {
            'name': 'Castrol EDGE LL',
            'category': 'Motor Yağı',
            'specs': '5W-30',
            'price': 1250.00,
            'image_url': 'castrol.avif'
        },
        {
            'name': 'Motul 8100 X-Clean EFE',
            'category': 'Motor Yağı',
            'specs': '5W-30',
            'price': 1650.00,
            'image_url': 'motul.webp'
        },
        {
            'name': 'Mobil 1 ESP',
            'category': 'Motor Yağı',
            'specs': '5W-30',
            'price': 1490.00,
            'image_url': 'mobil1.jpg'
        },
        {
            'name': 'Liqui Moly Top Tec 4200',
            'category': 'Motor Yağı',
            'specs': '5W-30',
            'price': 2100.00,
            'image_url': 'liqui-moly.webp'
        },
        # Lastikler
        {
            'name': 'Michelin Primacy 4+',
            'category': 'Lastik',
            'specs': '205/55 R16 91V',
            'price': 3450.00,
            'image_url': 'michelin.avif'
        },
        {
            'name': 'Lassa Snoways 4',
            'category': 'Lastik',
            'specs': '225/45 R17 94V XL',
            'price': 2850.00,
            'image_url': 'lassa.avif'
        },
        {
            'name': 'Goodyear Eagle Sport',
            'category': 'Lastik',
            'specs': '215/60 R17 96H',
            'price': 4100.00,
            'image_url': 'goodyear.avif'
        },
        {
            'name': 'Continental EcoContact 6',
            'category': 'Lastik',
            'specs': '195/65 R15 91H',
            'price': 2400.00,
            'image_url': 'continental.avif'
        },
        # Aküler
        {
            'name': 'Varta E11 Blue Dynamic',
            'category': 'Akü',
            'specs': '12V 74Ah',
            'price': 3200.00,
            'image_url': 'varta.jpg'
        },
        {
            'name': 'Mutlu Akü SAE',
            'category': 'Akü',
            'specs': '12V 50Ah',
            'price': 2450.00,
            'image_url': 'mutlu.png'
        },
        {
            'name': 'Bosch S4 005 Gümüş',
            'category': 'Akü',
            'specs': '12V 60Ah',
            'price': 2750.00,
            'image_url': 'bosch.avif'
        },
        {
            'name': 'İnci Akü Formul A',
            'category': 'Akü',
            'specs': '12V 72Ah',
            'price': 2900.00,
            'image_url': 'inci.jpg'
        }
    ]

    all_vehicles = Vehicle.query.all()
    print(f"Found {len(all_vehicles)} vehicles to associate products with.")

    for p_data in default_products:
        p = Product(
            name=p_data['name'],
            category=p_data['category'],
            specs=p_data['specs'],
            price=p_data['price'],
            image_url=p_data['image_url']
        )
        # Her ürünü mevcut tüm araçlara uyumlu olarak bağlıyoruz
        for v in all_vehicles:
            p.compatible_vehicles.append(v)
        db.session.add(p)

    db.session.commit()
    print("Default products successfully seeded and linked to all vehicles!")
