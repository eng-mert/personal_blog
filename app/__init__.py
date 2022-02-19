from flask import Flask
from config import Config
from database import Database
from .public import public_blueprint
from .dashboard import dashboard_blueprint
from .auth import auth_blueprint

app = Flask(__name__)
app.config.from_object(Config)


@app.before_first_request
def init_database():
    Database.initialize()


app.register_blueprint(public_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(auth_blueprint)
