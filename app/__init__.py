from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.static_folder = 'static'

application.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

login_manager = LoginManager()
login_manager.login_view = 'aplication.login'
login_manager.init_app(application)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes