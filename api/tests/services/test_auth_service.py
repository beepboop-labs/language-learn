from app.models.user import User
from app.services.auth_service import login_user, register_user
from app import db

# SAMPLE CODE FOR INTERACTING WITH DATABASE
# def test_create_user(client):
#     with client.application.app_context():
#         # Create a new user
#         new_user = User(username='test_user', password='bad_password')
#         db.session.add(new_user)
#         db.session.commit()

#         # Query the user from the database
#         user_from_db = User.query.filter_by(username='test_user').first()

#         # Check that the added properties match
#         assert user_from_db.username == new_user.username
#         assert user_from_db.password == new_user.password

# class TestLogin:
#     # test user credentials
#     # *********************
#     # username: test
#     # password: password

#     def test_success(client):
#         assert True

#     def test_wrong_username(client):
#         assert True

#     def test_wrong_password(client):
#         assert True

#     def test_empty_username(client):
#         assert True

#     def test_empty_password(client):
#         assert True

#     def test_returns_user_token(client):
#         assert True

# class TestRegister:

#     def test_success(client):
#         assert True

#     def test_existing_username(client):
#         assert True

#     def test_empty_username(client):
#         assert True

#     def test_empty_password(client):
#         assert True

#     def test_returns_user_token(client):
#         assert True


