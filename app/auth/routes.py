from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Geçersiz e-posta adresi veya şifre.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember.data)
        flash('Başarıyla giriş yaptınız!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('auth/login.html', title='Giriş Yap', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız.', 'info')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt işleminiz başarıyla tamamlandı! Şimdi giriş yapabilirsiniz.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Kayıt Ol', form=form)
