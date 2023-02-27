from flask import Flask, render_template
from flask import request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# Your Flask app code goes here


# Define the create_user function
def create_user(username, password):

    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS users''')
    
    # Creare a users table
    cursor.execute('''CREATE TABLE users
             (username TEXT, password TEXT)''')

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Create a new user in the database
        create_user(username, password)

        # Redirect to the login page
        return redirect('/login')
    # handle the sign-up process
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the user's entered username and password are valid
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user is not None and user[1] == password:
            # Log the user in and redirect to the dashboard
            session['username'] = username
            return 'Welcome to the quiz'
        else:
            # Display an error message
            return 'Invalid username or password.'
    else:
        # Render the login form
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
