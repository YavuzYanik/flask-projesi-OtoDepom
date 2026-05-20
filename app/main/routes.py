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
    return render_template('main/index.html', title='Ana Sayfa')

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
        
        # Eklenen aracı mevcut tüm ürünlere uyumlu olarak bağla
        all_products = Product.query.all()
        for p in all_products:
            vehicle.compatible_products.append(p)

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
    
    # Kullanıcının araçlarını yükle
    user_vehicles = []
    if current_user.is_authenticated:
        user_vehicles = current_user.vehicles

    if selected_vehicle_id:
        vehicle = db.session.get(Vehicle, selected_vehicle_id)
        if vehicle:
            products_list = vehicle.compatible_products
        else:
            products_list = Product.query.all()
    else:
        products_list = Product.query.all()

    # Kategorilere ayır
    tires = [p for p in products_list if p.category == 'Lastik']
    oils = [p for p in products_list if p.category == 'Motor Yağı']
    batteries = [p for p in products_list if p.category == 'Akü']

    return render_template('main/products.html', title='Ürünler',
                           tires=tires, oils=oils, batteries=batteries,
                           user_vehicles=user_vehicles, selected_vehicle_id=selected_vehicle_id)

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
            image_url=filename
        )

        # Yeni ürünü mevcut tüm araçlara uyumlu olarak bağla
        all_vehicles = Vehicle.query.all()
        for v in all_vehicles:
            product.compatible_vehicles.append(v)

        db.session.add(product)
        db.session.commit()
        flash('Yeni ürün başarıyla eklendi ve tüm araçlara tanımlandı!', 'success')
        return redirect(url_for('main.admin_products'))

    products_list = Product.query.all()
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
            product.image_url = filename

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

