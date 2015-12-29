from flask_wtf import Form
from wtforms import TextField, PasswordField,validators
from wtforms.validators import DataRequired,Email

class RegistrationForm(Form):
    fullname = TextField("Fullname",[validators.Length(min=5, max=60),DataRequired()])
    username = TextField("Username",[validators.Length(min=3, max=30),DataRequired()])
    email = TextField("Email",[DataRequired(),Email(message="Invalid Email")    ])
    password = PasswordField("Password",[
    validators.Required(),validators.EqualTo('confirm',message="Password must match")
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    username = TextField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class PostForm(Form):
    body = TextField("Body", validators=[DataRequired()])

class UpdateForm(Form):
    fullname = TextField("Fullname")
    phone = TextField("Phone")
    location = TextField("Location")
    website = TextField("Website")
    about = TextField("About")
