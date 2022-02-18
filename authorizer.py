from models import User
from flask import session, redirect, url_for, flash
from functools import wraps


class Authorizer:
    current_user = None

    @classmethod
    def register(cls, email, password):
        try:
            if User.find_one(email=email): return
            new_user = User(email=email)
            new_user.set_password(password=password)
            new_user.save_to_db()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def login(cls, email, password, remember_me):
        user = User.find_one(email=email)
        if not user: return
        if user.check_password(password=password):
            session['email'] = email
            cls.current_user = user
            if remember_me:
                session.permanent = True

    @classmethod
    def logout(cls):
        session.pop('email', None)
        cls.current_user = None
        pass

    @classmethod
    def rest_password(cls, email, password, new_password):
        user = User.find_one(email=email)
        if not user: return
        if password == user.password:
            user.update(password=new_password)

    @classmethod
    def admin_only(cls, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if cls.current_user and cls.current_user.is_admin:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('main.index'))

        return decorated_function

    @classmethod
    def login_required(cls, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if cls.current_user:
                return func(*args, **kwargs)
            else:
                flash('Login First', 'warning')
                return redirect(url_for('auth.login'))

        return decorated_function
