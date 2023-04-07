from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    spanish_prog = db.Column(db.Integer, db.ForeignKey('Spanish_Progress.spanish_id'),nullable=False)
    swahili_prog = db.Column(db.Integer, db.ForeignKey('Swahili_Progress.swahili_id'),nullable=False)

class Spanish_Progress(db.Model):
    spanish_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u1_mcq = db.Column(db.String(50))
    u1_filling = db.Column(db.String(100))
 
class Swahili_Progress(db.Model):
    swahili_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u1_mcq = db.Column(db.String(50))
    u1_filling = db.Column(db.String(100))
