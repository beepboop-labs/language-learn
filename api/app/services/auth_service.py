from app.models.user import User, db
from flask import make_response

def register_user(userdata):
    try:
        # Check if username already exists
        user_check = db.session.execute(db.select(User).filter_by(username=userdata['username'])).scalar()
        print(user_check)
        if user_check:
            return {"status": 409, "message": "username already exists"}
        else:
            username = userdata['username']
            password = userdata['password']

            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()

            return make_response({'message': f"New user: {new_user.username} successfully created"}, 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)
    
def login_user(credentials):
    try:
        # Check if username already exists
        user = db.session.execute(db.select(User).filter_by(username=credentials['username'])).scalar()
        print(user)
        if not user:
            return {"status": 404, "message": "username not found"}
        else:
            #TODO: use seperate method for hashing and validating password
            #TODO: login should return JWT token or something. Right now it doesnt do anything
            # Check password
            if credentials['password'] == user.password:
                return make_response({'message': 'User successfully authenticated'}, 200)
            else:
                return make_response({'message': 'Incorrect password'}, 200)

    except Exception as e:
        return make_response({'message': str(e)}, 500)