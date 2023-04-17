from flask import request, make_response
from flask import current_app as app
from app.services.user_service import get_activity,complete_quiz

@app.route('/user/activity', methods=['POST'])
def activity():
    request_data = request.get_json()
    response = get_activity(request_data)
    return response


@app.route('/user/complete-quiz', methods=['POST'])
def complete():
    request_data = request.get_json()
    response = complete_quiz(request_data)
    return response