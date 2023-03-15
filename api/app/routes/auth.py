from flask import request, make_response
from datetime import datetime as dt

#TODO: Fix this. There is no 'current_app'
from flask import current_app as app
from ..models.user import User, db

@app.route('/register', methods=['POST'])
def register_user():
    """Create a user from request json body."""
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    #TODO: Check if username already exists

    if username and password:
        new_user = User(
            username=username,
            password=password
        )

        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_user} successfully created")
    else:
        return make_response("Failed to create user")

@app.route('/login', methods=['POST'])
def login():
    """Login a user from request json body."""
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    if username and password:
        #TODO Validate username and password

        return make_response(f"{username} successfully logged in")
    else:
        return make_response("Failed to login")