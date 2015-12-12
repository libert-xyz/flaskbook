from wtforms import Form, TextField, PasswordField,validator

class RegistrationForm(Form):
    fullname = TextField()
