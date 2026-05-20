from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.models import Vehicle, VehicleNotification
from app.main.forms import VehicleForm, NotificationForm

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
    return render_template('main/products.html', title='Ürünler')
