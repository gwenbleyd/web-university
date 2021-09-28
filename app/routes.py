from app import application
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required, current_user


@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html')


@application.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('Пожалуйста проверьте ваш логин или пароль')
        return redirect(url_for('home'))
    elif check_password_hash(user.password, password):
        login_user(user, remember=True)
        return redirect(url_for('profile'))
    else:
        flash('Пожалуйста проверьте ваш логин или пароль')
        return redirect(url_for('home'))


@application.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', name=current_user.name, surname=current_user.surname,
                               email=current_user.email)
    else:
        return redirect(url_for('register'))


@application.route('/register')
def register():
    return render_template('register.html')


@application.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    surname = request.form.get('surname')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('register'))

    new_user = User(email=email, password=generate_password_hash(password, method='sha256'), name=name,
                    surname=surname)

    db.session.add(new_user)
    db.session.commit()
    login_user(user, remember=True)

    return redirect(url_for('profile'))


@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))