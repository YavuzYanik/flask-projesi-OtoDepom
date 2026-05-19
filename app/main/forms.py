from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class VehicleForm(FlaskForm):
    brand = StringField('Marka (Örn: Ford)', validators=[DataRequired()])
    model_name = StringField('Model (Örn: Focus)', validators=[DataRequired()])
    year = IntegerField('Yıl', validators=[DataRequired(), NumberRange(min=1950, max=2026)])
    inspection_date = DateField('Sonraki Muayene Tarihi', format='%Y-%m-%d', validators=[DataRequired()])
    maintenance_date = DateField('Sonraki Yağ Bakım Tarihi', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Aracı Kaydet')

class NotificationForm(FlaskForm):
    title = StringField('Bildirim Başlığı (Örn: Triger Kayışı)', validators=[DataRequired()])
    due_date = DateField('Tarih', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Bildirim Ekle')
