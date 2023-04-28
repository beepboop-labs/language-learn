from flask import make_response, jsonify
from app.models.language import Language
from app import db
from app.models.activity import Activity
import json
from app.models.user import User


def get_activity(user):
    try:
        #open a sample data file
        f = open('data/sample_user_data.json')
        user_activity = json.load(f)

        #user_activity= {}
    
        print(user,flush=True)
        return make_response(jsonify(user_activity), 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)
    

def complete_quiz(data):
    try:
        if 'userid' not in data or 'language' not in data or 'unit' not in data or 'quiz' not in data:
            return make_response("userid, language, unit, and quiz required", 400)
        
        if data['quiz'] not in [1, 2, 3]:
            return make_response("Invalid quiz. Only '1', '2', and '3' available.", 400)
        if data['unit'] not in [1, 2, 3]:
            return make_response("Invalid unit. Only '1', '2', and '3' available.", 400)

        user = User.query.filter_by(id=data['userid']).first()
        if not user:
            return make_response("User not found",400)

        unit = data['unit']
        quiz = data['quiz']

        user_id = data['userid']
        
        language = Language.query.filter_by(name=data['language']).first()

        if not language:
            return make_response("Language not found", 400)

        activity = Activity.query.filter_by(user_id = user_id,language_id = language.id).first()
        print(activity)
        if unit == 1:
            if quiz == 1:
                activity.unit1_quiz1 = True
            elif quiz == 2:
                activity.unit1_quiz2 = True
            elif quiz == 3:
                activity.unit1_quiz3 = True
        elif unit == 2:
            if quiz == 1:
                activity.unit2_quiz1 = True
            elif quiz == 2:
                activity.unit2_quiz2 = True
            elif quiz == 3:
                activity.unit2_quiz3 = True
        elif unit == 3: 
            if quiz == 1:
                activity.unit3_quiz1 = True
            elif quiz == 2:
                activity.unit3_quiz2 = True
            elif quiz == 3:
                activity.unit3_quiz3 = True
        db.session.add(activity)
        db.session.commit()
        print(quiz,flush=True)
        return make_response("Record Updated Successfully", 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)