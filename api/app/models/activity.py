from app import db
# from app.models.language import Language
# from app.models.user import User

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language_id = db.Column(db.Integer, db.ForeignKey('Language.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    unit1_quiz1 = db.Column(db.Boolean, default=False);
    unit1_quiz2 = db.Column(db.Boolean, default=False);
    unit1_quiz3 = db.Column(db.Boolean, default=False);
    unit2_quiz1 = db.Column(db.Boolean, default=False);
    unit2_quiz2 = db.Column(db.Boolean, default=False);
    unit2_quiz3 = db.Column(db.Boolean, default=False);
    unit3_quiz1 = db.Column(db.Boolean, default=False);
    unit3_quiz2 = db.Column(db.Boolean, default=False);
    unit3_quiz3 = db.Column(db.Boolean, default=False);

def __repr__(self):
        return '<Activity %r>' % self.user_id % self.language_id