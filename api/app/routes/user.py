from flask import request, make_response
from flask import current_app as app
from app.services.user_service import get_activity

@app.route('/user/activity', methods=['POST'])
def activity():
    request_data = request.get_json()
    response = get_activity(request_data)
    return response