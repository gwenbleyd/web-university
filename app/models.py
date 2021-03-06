from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), default=None)
    surname = db.Column(db.String(100), default=None)
    password = db.Column(db.String(100))