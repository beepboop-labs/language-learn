from app.models.user import User
from app import db

def test_helloworld():
    assert True == True

def test_create_user(client):
    with client.application.app_context():
        # Create a new user
        new_user = User(username='test_user', password='bad_password')
        db.session.add(new_user)
        db.session.commit()

        # Query the user from the database
        user_from_db = User.query.filter_by(username='test_user').first()

        # Check that the added properties match
        assert user_from_db.username == new_user.username
        assert user_from_db.password == new_user.password
