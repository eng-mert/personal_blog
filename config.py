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

    # S3 Keys
    ACCESS_KEY_ID = 'AKIA6QEZ4CYFPTDI6BBL'
    ACCESS_SECRET_KEY = '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'
    S3_BUCKET_NAME = "flask-buk"
    S3_LOCATION = f"https://{S3_BUCKET_NAME}.s3.us-west-1.amazonaws.com/"
