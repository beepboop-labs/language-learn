from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from ..config import Development, Production


db = SQLAlchemy()
migrate = Migrate()

def create_app( ):
    app = Flask(__name__)
    app.config.from_object('config.Development')
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from  app.routes import auth, quiz, user
        db.create_all()  # Create sql tables for our data models

    return app