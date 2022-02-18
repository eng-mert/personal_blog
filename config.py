from datetime import timedelta


class Config:
    SECRET_KEY = 'my-secret-key'
    SECURITY_PASSWORD_SALT = 'SECURITY_PASSWORD_SALT'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = "mertyuusf@gmail.com"
    MAIL_PASSWORD = "05314847769Mert"
