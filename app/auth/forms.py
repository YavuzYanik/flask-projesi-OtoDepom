from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User

class RegisterForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('E-posta Adresi', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Şifreyi Onayla', validators=[DataRequired(), EqualTo('password', message='Şifreler eşleşmiyor.')])
    submit = SubmitField('Kayıt Ol')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Bu e-posta adresi zaten kullanılıyor. Lütfen başka bir e-posta girin veya giriş yapın.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Bu kullanıcı adı alınmış. Lütfen başka bir tane seçin.')

class LoginForm(FlaskForm):
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')
