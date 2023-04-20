from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app import models
# from ..config import Development, Production


db = SQLAlchemy()
migrate = Migrate()

def create_app(config='config.Development'):
    app = Flask(__name__)
    
    # Configure the flask app instance
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    CORS(app)
    
    with app.app_context():
        from  app.routes import auth, quiz, user

    return app