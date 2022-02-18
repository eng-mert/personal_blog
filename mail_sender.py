from flask import url_for, render_template
from itsdangerous import URLSafeTimedSerializer

from app.models.user import User
from config import Config
import smtplib
from email.message import EmailMessage


class MailSender:
    salt_key = Config.SECURITY_PASSWORD_SALT
    secret_key = Config.SECRET_KEY

    @classmethod
    def generate_confirmation_token(cls, email):
        serializer = URLSafeTimedSerializer(secret_key=cls.secret_key)
        token = serializer.dumps(email, salt=cls.salt_key)
        return token

    @classmethod
    def confirm_token(cls, token, expiration=3600):
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        try:
            email = serializer.loads(token,
                                     salt=cls.salt_key,
                                     max_age=expiration)
            return User.find_one(email=email)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def send_confirmation_token(cls, email):
        token = cls.generate_confirmation_token(email)
        msg = EmailMessage()
        msg['Subject'] = "Please confirm your email"
        msg['FROM'] = Config.MAIL_USERNAME
        msg['TO'] = email
        html_msg = render_template('includes/_confirmation_msg.html', token=token)
        msg.add_alternative(html_msg, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
            smtp.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            smtp.send_message(msg)

    @classmethod
    def send_rest_request_url(cls, email):
        token = cls.generate_confirmation_token(email)
        msg = EmailMessage()
        msg['Subject'] = "Rest Your Password"
        msg['FROM'] = Config.MAIL_USERNAME
        msg['TO'] = email
        content = f"""
To rest your password follow click the link :
{url_for('auth.rest_password',token=token,_external=True)}
"""
        msg.set_content(content)
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
            smtp.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            smtp.send_message(msg)