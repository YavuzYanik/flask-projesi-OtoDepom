from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.models import Vehicle, VehicleNotification, Product
from app.main.forms import VehicleForm, NotificationForm
from werkzeug.utils import secure_filename
import os

@main.route('/')
@main.route('/index')
def index():
    popular_products = Product.query.limit(4).all()
    return render_template('main/index.html', title='Ana Sayfa', popular_products=popular_products)

@main.route('/garage')
@login_required
def garage():
    vehicles = current_user.vehicles
    return render_template('main/garage.html', title='Garajım', vehicles=vehicles)

from app.cars_data import CAR_DATA
from datetime import datetime

@main.route('/garage/add', methods=['GET', 'POST'])
@login_required
def garage_add():
    if request.method == 'POST':
        brand = request.form.get('brand')
        series = request.form.get('series')
        model_name = request.form.get('model_name')
        year = request.form.get('year')
        plate = request.form.get('plate')
        fuel_type = request.form.get('fuel_type')
        transmission = request.form.get('transmission')
        engine_power = request.form.get('engine_power')
        inspection_date_str = request.form.get('inspection_date')
        maintenance_date_str = request.form.get('maintenance_date')

        # Model ismini "Series - Model" şeklinde birleştirerek kaydet
        full_model_name = f"{series} - {model_name}" if series and model_name else (model_name or series or "Belirtilmedi")

        try:
            insp_date = datetime.strptime(inspection_date_str, '%Y-%m-%d').date() if inspection_date_str else None
            maint_date = datetime.strptime(maintenance_date_str, '%Y-%m-%d').date() if maintenance_date_str else None
        except ValueError:
            insp_date = None
            maint_date = None

        vehicle = Vehicle(
            brand=brand,
            model_name=full_model_name,
            year=int(year) if year else 0,
            plate=plate,
            fuel_type=fuel_type,
            transmission=transmission,
            engine_power=engine_power,
            inspection_date=insp_date,
            maintenance_date=maint_date,
            owner=current_user
        )
        
        # Uyumlu ürünleri otomatik olarak bağla
        from app.cars_data import link_vehicle_products
        link_vehicle_products(vehicle)

        db.session.add(vehicle)
        db.session.commit()
        flash('Aracınız başarıyla garaja eklendi!', 'success')
        return redirect(url_for('main.garage'))
        
    return render_template('main/garage_add.html', 
                          title='Araç Ekle',
                          car_data=CAR_DATA)

@main.route('/garage/vehicle/<int:id>', methods=['GET', 'POST'])
@login_required
def garage_detail(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle or vehicle.owner != current_user:
        flash('Araç bulunamadı veya yetkiniz yok.', 'danger')
        return redirect(url_for('main.garage'))
    
    form = NotificationForm()
    if form.validate_on_submit():
        notif = VehicleNotification(
            title=form.title.data,
            due_date=form.due_date.data,
            vehicle=vehicle
        )
        db.session.add(notif)
        db.session.commit()
        flash('Bildirim başarıyla eklendi.', 'success')
        return redirect(url_for('main.garage_detail', id=vehicle.id))
        
    return render_template('main/garage_detail.html', title=f'{vehicle.brand} {vehicle.model_name}', vehicle=vehicle, form=form)

@main.route('/garage/vehicle/<int:id>/delete', methods=['POST'])
@login_required
def vehicle_delete(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle or vehicle.owner != current_user:
        flash('Bu işlem için yetkiniz yok!', 'danger')
        return redirect(url_for('main.garage'))
    
    db.session.delete(vehicle)
    db.session.commit()
    flash('Araç başarıyla garajınızdan silindi.', 'success')
    return redirect(url_for('main.garage'))

@main.route('/garage/vehicle/<int:id>/update_dates', methods=['POST'])
@login_required
def update_dates(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle or vehicle.owner != current_user:
        flash('Bu işlem için yetkiniz yok!', 'danger')
        return redirect(url_for('main.garage'))

    inspection_date_str = request.form.get('inspection_date')
    maintenance_date_str = request.form.get('maintenance_date')

    try:
        if inspection_date_str:
            vehicle.inspection_date = datetime.strptime(inspection_date_str, '%Y-%m-%d').date()
        else:
            vehicle.inspection_date = None

        if maintenance_date_str:
            vehicle.maintenance_date = datetime.strptime(maintenance_date_str, '%Y-%m-%d').date()
        else:
            vehicle.maintenance_date = None
            
        db.session.commit()
        flash('Araç tarihleri başarıyla güncellendi.', 'success')
    except ValueError:
        flash('Geçersiz tarih formatı!', 'danger')

    return redirect(url_for('main.garage_detail', id=vehicle.id))

@main.route('/products')
def products():
    selected_vehicle_id = request.args.get('vehicle_id', type=int)
    manual_brand  = request.args.get('brand', '')
    manual_series = request.args.get('series', '')
    manual_motor  = request.args.get('motor', '')

    user_vehicles = []
    if current_user.is_authenticated:
        user_vehicles = current_user.vehicles

    from app.cars_data import CAR_DATA
    import json

    manual_specs = None
    if manual_brand and manual_series and manual_motor:
        try:
            manual_specs = CAR_DATA[manual_brand][manual_series][manual_motor]
        except KeyError:
            manual_specs = None

    if selected_vehicle_id:
        vehicle = db.session.get(Vehicle, selected_vehicle_id)
        if vehicle:
            products_list = vehicle.compatible_products
        else:
            products_list = Product.query.all()
    elif manual_specs:
        oil_spec     = manual_specs.get('oil', '')
        battery_spec = manual_specs.get('battery', '')
        tire_spec    = manual_specs.get('tire', '')
        all_p = Product.query.all()
        products_list = []
        for p in all_p:
            if p.category == 'Motor Yagi' and oil_spec and oil_spec.lower() in p.specs.lower():
                products_list.append(p)
            elif p.category == 'Motor Yağı' and oil_spec and oil_spec.lower() in p.specs.lower():
                products_list.append(p)
            elif p.category == 'Akü' and battery_spec:
                v_num = ''.join(filter(str.isdigit, battery_spec))
                p_num = ''.join(filter(str.isdigit, p.specs))
                if v_num and p_num and v_num in p_num:
                    products_list.append(p)
            elif p.category == 'Lastik' and tire_spec and tire_spec.lower() in p.specs.lower():
                products_list.append(p)
            elif p.category == 'Diğer':
                products_list.append(p)
        if not products_list:
            products_list = Product.query.all()
    else:
        products_list = Product.query.all()

    tires     = [p for p in products_list if p.category == 'Lastik']
    oils      = [p for p in products_list if p.category == 'Motor Yağı']
    batteries = [p for p in products_list if p.category == 'Akü']
    others    = [p for p in products_list if p.category == 'Diğer']

    car_data_json = json.dumps(CAR_DATA, ensure_ascii=False)

    return render_template('main/products.html', title='Ürünler',
                           tires=tires, oils=oils, batteries=batteries, others=others,
                           user_vehicles=user_vehicles, selected_vehicle_id=selected_vehicle_id,
                           car_data_json=car_data_json,
                           manual_brand=manual_brand, manual_series=manual_series,
                           manual_motor=manual_motor, manual_specs=manual_specs)

@main.route('/category/<string:category_name>')
def category_products(category_name):
    category_map = {
        'motor-yaglari': 'Motor Yağı',
        'lastikler': 'Lastik',
        'akuler': 'Akü',
        'diger-urunler': 'Diğer'
    }
    db_cat = category_map.get(category_name)
    if not db_cat:
        flash('Geçersiz kategori!', 'danger')
        return redirect(url_for('main.products'))
        
    page = request.args.get('page', 1, type=int)
    products_paginate = Product.query.filter_by(category=db_cat).paginate(page=page, per_page=12, error_out=False)
    
    title_map = {
        'Motor Yağı': 'Motor Yağları',
        'Lastik': 'Otomobil & SUV Lastikleri',
        'Akü': 'Aküler',
        'Diğer': 'Diğer Ürünler'
    }
    
    return render_template('main/category.html', title=title_map[db_cat], products=products_paginate, category_slug=category_name)

@main.route('/about')
def about():
    return render_template('main/about.html', title='Hakkımızda')

# --- ADMIN ROUTELARI ---
@main.route('/admin/products', methods=['GET', 'POST'])
@login_required
def admin_products():
    # Admin kontrolü: Kullanıcı adı 'admin' olan veya is_admin bayrağı True olan girebilir
    if not current_user.is_admin and current_user.username != 'admin':
        flash('Bu alana erişim yetkiniz yok!', 'danger')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        specs = request.form.get('specs')
        
        # Fiyattaki binlik ayıracı (virgül) temizleme işlemi
        price_str = request.form.get('price')
        price = 0.0
        if price_str:
            try:
                price = float(price_str.replace(',', ''))
            except ValueError:
                price = 0.0
                
        stock = request.form.get('stock', 10, type=int)
        
        # Görsel yükleme işlemi
        file = request.files.get('image')
        filename = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'products')
            os.makedirs(upload_folder, exist_ok=True)
            file.save(os.path.join(upload_folder, filename))

        product = Product(
            name=name,
            category=category,
            specs=specs,
            price=price,
            stock=stock,
            image_url=filename
        )

        db.session.add(product)
        db.session.commit()

        # Uyumlu araçları dinamik olarak bağla
        from app.cars_data import link_vehicle_products
        all_vehicles = Vehicle.query.all()
        for v in all_vehicles:
            link_vehicle_products(v)
        db.session.commit()

        flash('Yeni ürün başarıyla eklendi ve uyumlu araçlara tanımlandı!', 'success')
        return redirect(url_for('main.admin_products'))

    page = request.args.get('page', 1, type=int)
    products_list = Product.query.paginate(page=page, per_page=10, error_out=False)
    return render_template('main/admin_products.html', title='Ürün Yönetimi', products=products_list)

@main.route('/admin/products/edit/<int:id>', methods=['POST'])
@login_required
def admin_products_edit(id):
    if not current_user.is_admin and current_user.username != 'admin':
        flash('Yetkisiz işlem!', 'danger')
        return redirect(url_for('main.index'))

    product = db.session.get(Product, id)
    if not product:
        flash('Ürün bulunamadı.', 'danger')
        return redirect(url_for('main.admin_products'))

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.category = request.form.get('category')
        product.specs = request.form.get('specs')
        product.stock = request.form.get('stock', product.stock, type=int)
        
        # Fiyattaki binlik ayıracı (virgül) temizleme işlemi
        price_str = request.form.get('price')
        if price_str:
            try:
                product.price = float(price_str.replace(',', ''))
            except ValueError:
                pass

        file = request.files.get('image')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'products')
            os.makedirs(upload_folder, exist_ok=True)
            file.save(os.path.join(upload_folder, filename))
        db.session.commit()

        # Uyumlu araçları dinamik olarak güncelle
        from app.cars_data import link_vehicle_products
        all_vehicles = Vehicle.query.all()
        for v in all_vehicles:
            link_vehicle_products(v)
        db.session.commit()

        flash('Ürün başarıyla güncellendi!', 'success')

    return redirect(url_for('main.admin_products'))

@main.route('/admin/products/delete/<int:id>', methods=['POST'])
@login_required
def product_delete(id):
    if not current_user.is_admin and current_user.username != 'admin':
        flash('Yetkisiz işlem!', 'danger')
        return redirect(url_for('main.index'))

    product = db.session.get(Product, id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Ürün başarıyla silindi.', 'success')
    else:
        flash('Ürün bulunamadı.', 'danger')
    return redirect(url_for('main.admin_products'))


@main.context_processor
def inject_notifications():
    notifications = []
    if current_user.is_authenticated:
        from datetime import date
        today = date.today()
        for vehicle in current_user.vehicles:
            # Muayene Tarihi Kontrolü (Son 30 gün kala veya geçmişse)
            if vehicle.inspection_date:
                days_left = (vehicle.inspection_date - today).days
                if 0 <= days_left <= 30:
                    notifications.append({
                        'type': 'inspection',
                        'vehicle_id': vehicle.id,
                        'brand': vehicle.brand,
                        'model_name': vehicle.model_name,
                        'plate': vehicle.plate or '',
                        'days_left': days_left,
                        'title': f'{vehicle.brand} Muayene Yaklaşıyor!',
                        'text': f'Muayene tarihine {days_left} gün kaldı ({vehicle.inspection_date.strftime("%d.%m.%Y")}).'
                    })
                elif days_left < 0:
                    notifications.append({
                        'type': 'inspection_overdue',
                        'vehicle_id': vehicle.id,
                        'brand': vehicle.brand,
                        'model_name': vehicle.model_name,
                        'plate': vehicle.plate or '',
                        'days_left': days_left,
                        'title': f'{vehicle.brand} Muayenesi Gecikmiş!',
                        'text': f'Muayene tarihi {-days_left} gün önceydi ({vehicle.inspection_date.strftime("%d.%m.%Y")})!'
                    })
            
            # Bakım Tarihi Kontrolü (Son 30 gün kala veya geçmişse)
            if vehicle.maintenance_date:
                days_left = (vehicle.maintenance_date - today).days
                if 0 <= days_left <= 30:
                    notifications.append({
                        'type': 'maintenance',
                        'vehicle_id': vehicle.id,
                        'brand': vehicle.brand,
                        'model_name': vehicle.model_name,
                        'plate': vehicle.plate or '',
                        'days_left': days_left,
                        'title': f'{vehicle.brand} Bakım Zamanı Yaklaşıyor!',
                        'text': f'Bakım zamanına {days_left} gün kaldı ({vehicle.maintenance_date.strftime("%d.%m.%Y")}).'
                    })
                elif days_left < 0:
                    notifications.append({
                        'type': 'maintenance_overdue',
                        'vehicle_id': vehicle.id,
                        'brand': vehicle.brand,
                        'model_name': vehicle.model_name,
                        'plate': vehicle.plate or '',
                        'days_left': days_left,
                        'title': f'{vehicle.brand} Bakımı Gecikmiş!',
                        'text': f'Periyodik bakım tarihi {-days_left} gün önceydi ({vehicle.maintenance_date.strftime("%d.%m.%Y")})!'
                    })
    return dict(user_notifications=notifications)

@main.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html', title='Profilim')

@main.route('/cart')
@login_required
def view_cart():
    from app.models import CartItem
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    return render_template('main/cart.html', title='Sepetim', cart_items=cart_items, total_price=total_price)

@main.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    from app.models import CartItem, Product
    product = db.session.get(Product, product_id)
    if not product:
        flash('Ürün bulunamadı!', 'danger')
        return redirect(url_for('main.products'))

    qty_to_add = int(request.form.get('quantity', 1))

    if product.stock < qty_to_add:
        flash(f'Yetersiz stok! Sadece {product.stock} adet eklenebilir.', 'warning')
        return redirect(url_for('main.product_detail', id=product_id))
    
    # Check if item is already in cart
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        if cart_item.quantity + qty_to_add > product.stock:
            flash(f'Sepetinizdeki miktar ile birlikte stok sınırı aşılıyor! (Maks: {product.stock})', 'warning')
            return redirect(url_for('main.product_detail', id=product_id))
        cart_item.quantity += qty_to_add
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=qty_to_add)
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{qty_to_add} adet ürün sepete eklendi!', 'success')
    return redirect(url_for('main.product_detail', id=product_id))

@main.route('/cart/increase/<int:item_id>', methods=['POST'])
@login_required
def increase_cart(item_id):
    from app.models import CartItem
    cart_item = db.session.get(CartItem, item_id)
    if cart_item and cart_item.user_id == current_user.id:
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            db.session.commit()
        else:
            flash('Maksimum stok miktarına ulaşıldı.', 'warning')
    return redirect(url_for('main.view_cart'))

@main.route('/cart/decrease/<int:item_id>', methods=['POST'])
@login_required
def decrease_cart(item_id):
    from app.models import CartItem
    cart_item = db.session.get(CartItem, item_id)
    if cart_item and cart_item.user_id == current_user.id:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            db.session.commit()
        else:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Ürün sepetten çıkarıldı.', 'success')
    return redirect(url_for('main.view_cart'))

@main.route('/cart/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    from app.models import CartItem
    cart_item = db.session.get(CartItem, item_id)
    if cart_item and cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Ürün sepetten çıkarıldı.', 'success')
    return redirect(url_for('main.view_cart'))

@main.route('/product/<int:id>')
def product_detail(id):
    from app.models import Product
    product = db.session.get(Product, id)
    if not product:
        flash('Ürün bulunamadı.', 'danger')
        return redirect(url_for('main.products'))
    return render_template('main/product_detail.html', title=product.name, product=product)

@main.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    from app.models import CartItem, OrderGroup, Order
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Sepetiniz boş!', 'warning')
        return redirect(url_for('main.products'))
        
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    
    if request.method == 'POST':
        address = request.form.get('address')
        city = request.form.get('city')
        phone = request.form.get('phone')
        
        if not address or not city or not phone:
            flash('Lütfen tüm adres ve iletişim bilgilerini doldurun.', 'danger')
            return redirect(url_for('main.checkout'))
            
        # Create OrderGroup
        order_group = OrderGroup(
            user_id=current_user.id,
            address=address,
            city=city,
            phone=phone,
            total_price=total_price,
            status='Beklemede'
        )
        db.session.add(order_group)
        db.session.flush() # get id
        
        # Move CartItems to Orders and decrement stock
        for item in cart_items:
            # Check stock one last time
            if item.product.stock < item.quantity:
                db.session.rollback()
                flash(f'{item.product.name} için yeterli stok yok! Mevcut: {item.product.stock}', 'danger')
                return redirect(url_for('main.view_cart'))
                
            order = Order(
                user_id=current_user.id,
                product_id=item.product_id,
                order_group_id=order_group.id,
                quantity=item.quantity,
                price_at_purchase=item.product.price
            )
            item.product.stock -= item.quantity
            db.session.add(order)
            db.session.delete(item)
            
        db.session.commit()
        flash('Siparişiniz başarıyla alındı! Teşekkür ederiz.', 'success')
        return redirect(url_for('main.profile'))
        
    return render_template('main/checkout.html', title='Siparişi Tamamla', cart_items=cart_items, total_price=total_price)

@main.route('/admin/orders')
@login_required
def admin_orders():
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Yetkisiz erişim.', 'danger')
        return redirect(url_for('main.index'))
    
    from app.models import OrderGroup
    page = request.args.get('page', 1, type=int)
    order_groups = OrderGroup.query.order_by(OrderGroup.order_date.desc()).paginate(page=page, per_page=10)
    
    return render_template('main/admin_orders.html', title='Sipariş Yönetimi', order_groups=order_groups)

@main.route('/admin/orders/update/<int:id>', methods=['POST'])
@login_required
def update_order_status(id):
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Yetkisiz erişim.', 'danger')
        return redirect(url_for('main.index'))
        
    from app.models import OrderGroup
    order_group = db.session.get(OrderGroup, id)
    if order_group:
        new_status = request.form.get('status')
        if new_status:
            order_group.status = new_status
            db.session.commit()
            flash('Sipariş durumu güncellendi.', 'success')
            
    return redirect(url_for('main.admin_orders'))
