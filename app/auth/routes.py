from flask import Blueprint, request, redirect, render_template, url_for, session

from app.models import User
from authorizer import Authorizer
from config import Config

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        new_user = User(email=email, first_name=first_name, last_name=last_name, is_admin=False)
        if confirm_password == password:
            new_user.set_password(password)
            new_user.save_to_db()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='register')


@auth_blueprint.route('/login', methods=['GET', 'POST', ])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        selected_user = User.find_one(email=email)
        if selected_user.check_password(password):
            session['email'] = email
            Authorizer.current_user = selected_user
            return redirect(url_for('dashboard.index'))
    return render_template('auth/login.html')


@auth_blueprint.route('/logout')
def logout():
    session.pop('email', None)
    Authorizer.logout()
    return redirect(url_for('public.index'))
