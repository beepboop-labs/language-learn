from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from ..config import Development, Production


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app( ):
    app = Flask(__name__)
    app.config.from_object(Development)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app