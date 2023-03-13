from flask import Flask, render_template
from flask import request, redirect, session
from flask import jsonify
from flask_cors import CORS
import json
import sqlite3

# SAMPLE QUIZ DATA
f = open('data.json')
quiz_data = json.load(f)


app = Flask(__name__)
CORS(app)

#TODO: STORE DB KEYS IN .ENV FILE
app.secret_key = 'my_secret_key'

# Define the create_user function
def create_user(username, password):

    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    #TODO: NEED TO CHECK IF USER ALREADY EXISTS/USERNAME TAKEN
    #TODO: ADD PASSWORD HASHING?

    # Insert a new user into the users table
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    ## TODO: ADD A TRY CATCH HERE

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Create a new user in the database
        create_user(username, password)

        return jsonify({'username': username,
                        'password': password}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():

    #TODO: SET UP JWT OR OTHER METHOD FOR CLIENT SIDE SESSION

    if request.method == 'POST':
        # Check if the user's entered username and password are valid
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user is not None and user[1] == password:
            # Log the user in and redirect to the dashboard
            session['username'] = username
            return jsonify({'message': 'Login Successful'})
        else:
            # Display an error message
            return jsonify({'message': 'Invalid username or password.'})


@app.route('/quizdata', methods=['POST'])

#TODO: ADD ARGUMENTS FOR QUIZ LENGTH, TYPE, ETC
def quizdata():
    if request.method == 'POST':
        return jsonify(quiz_data)


if __name__ == '__main__':
    app.run(debug=True)
