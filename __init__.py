from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from crud import views
