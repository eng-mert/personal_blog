from datetime import datetime
from hashlib import md5
from models import Model
from werkzeug.security import generate_password_hash, check_password_hash


class User(Model):
    collection = 'users'

    def __init__(self, email, password=None, confirmed=None, is_admin=False, first_name=None, last_name=None,
                 joined_date=None, image=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.is_admin = is_admin or False
        self.confirmed = confirmed or False
        self.first_name = first_name or ""
        self.last_name = last_name or ""
        self.image = image or self.avatar(64)
        self.joined_date = joined_date or datetime.utcnow().strftime('%Y-%m-%d')

    def set_password(self, password):
        self.password = generate_password_hash(password, 'sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_password(self, new_password):
        new_password = generate_password_hash(new_password, 'sha256')
        self.update(password=new_password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def to_json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin,
            'confirmed': self.confirmed,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'image': self.image,
            'joined_date': self.joined_date
        }