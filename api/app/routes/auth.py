from flask import request, make_response
from flask import current_app as app
from app.services.auth_service import register_user, login_user

@app.route('/register', methods=['POST'])
def register():
    request_data = request.get_json()
    response = register_user(request_data)
    return response

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    response = login_user(request_data)
    return response