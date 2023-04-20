from flask import make_response, jsonify
import json

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
    

def complete_quiz(quiz):
    try:
      
    
    
        print(quiz,flush=True)
        return make_response("Record Updated Successfully", 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)