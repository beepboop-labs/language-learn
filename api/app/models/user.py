from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    activities = db.relationship('Activity', backref='user', lazy=True)

 
    def __repr__(self):
        return '<User %r>' % self.username

