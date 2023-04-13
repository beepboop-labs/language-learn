from app.models.user import User
from app.services.auth_service import login_user, register_user
from app import db
import json

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

class TestLogin:
    # existing test user credentials
    # *********************
    # username: test
    # password: password

    def test_success(self, client):
        # Send a login request with the user credentials
        data = {'username': 'test', 'password': 'password'}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check that the response is successful
        assert response.status_code == 200

        # Check that the response contains the user token
        response_data = json.loads(response.data)
        assert 'username' in response_data
        assert 'id' in response_data

    def test_user_not_found(self, client):
      
        data = {'username': 'wrong', 'password': 'password'}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check response is unauthorized
        assert response.status_code == 401

    def test_wrong_password(self, client):
        data = {'username': 'test', 'password': 'wrong'}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check response is unauthorized
        assert response.status_code == 401

    def test_empty_username(self, client):
        data = {'username': '', 'password': 'wrong'}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check response is unauthorized
        assert response.status_code == 401

    def test_empty_password(self, client):
        data = {'username': 'test', 'password': ''}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check response is unauthorized
        assert response.status_code == 401

    def test_missing_property(self, client):
        data = {'username': 'test'}
        response = client.post('/login', data=json.dumps(data), content_type='application/json')

        # Check response is bad request
        assert response.status_code == 400


class TestRegister:
    # existing test user credentials
    # *********************
    # username: test
    # password: password

    def test_success(self, client):
        # Send a registers request with the user credentials
        data = {'username': 'new-user', 'password': 'password'}
        response = client.post('/register', data=json.dumps(data), content_type='application/json')

        # Check that the response is successful
        assert response.status_code == 200

        # Check that the response contains the user token
        response_data = json.loads(response.data)
        assert 'username' in response_data
        assert 'id' in response_data

    def test_existing_username(self, client):
        data = {'username': 'test', 'password': 'password'}
        response = client.post('/register', data=json.dumps(data), content_type='application/json')

        # Check response is conflict
        assert response.status_code == 409

    def test_empty_username(self, client):
        data = {'username': '', 'password': 'password'}
        response = client.post('/register', data=json.dumps(data), content_type='application/json')

        # Check response is bad request
        assert response.status_code == 400

    def test_empty_password(self, client):
        data = {'username': 'new-user', 'password': ''}
        response = client.post('/register', data=json.dumps(data), content_type='application/json')

        # Check response is bad request
        assert response.status_code == 400

    def test_missing_property(self, client):
        data = {'username': 'new-user'}
        response = client.post('/register', data=json.dumps(data), content_type='application/json')

        # Check response is bad request
        assert response.status_code == 400



