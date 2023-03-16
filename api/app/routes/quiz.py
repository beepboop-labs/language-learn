from flask import request, make_response
from flask import current_app as app
from app.services.quiz_service import get_quiz

@app.route('/quiz', methods=['POST'])
def quiz():

    #There is no request data right now.
    request_data = request.get_json()
    response = get_quiz(request_data)
    return response

