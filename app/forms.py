from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.Required(mesage='El password es requerido')
    ])
class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Email', [
        validators.length(min=6,max=100),
        validators.Required(message='El email es requerido.')
        validators.Email(message='Ingrese un email valido.')
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido.')
        validators.EqualTo('confirm_password', mesage='La contraseña no coincide.' )
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('Acepto terminos y condiciones', [
        validators.DataRequired()
    ])
