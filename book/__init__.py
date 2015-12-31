from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from .momentjs import momentjs



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.jinja_env.globals['momentjs'] = momentjs

from book import views,models

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter(models.User.id == int(user_id)).first()
