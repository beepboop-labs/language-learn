from flask import request, make_response

#TODO: Fix this. There is no 'current_app'
from flask import current_app as app
# from ..models.user import User, db

# SAMPLE QUIZ DATA
f = open('../../sample_data.json')
quiz_data = json.load(f)

@app.route('/quiz', methods=['POST'])
def quiz():
    """Login a user from request json body."""
    #There is no request data right now.
    #TODO: add logic to request different kinds of quiz data
    request_data = request.get_json()

    return jsonify(quiz_data)

