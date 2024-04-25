from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('databases/user_list/users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database for the user's credentials
    cursor.execute('SELECT * FROM user_list WHERE user = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    if user:
            privilege = user[3]
            print(privilege)
            if privilege == 15:
                return redirect(url_for('master', values=user[1]))
            elif privilege == 10:
                return redirect(url_for('player', username=user[1]))

    # Render the login page again with an error message
    error_message = "Invalid username or password. Please try again."
    return render_template('index.html',
                           error=error_message)

@app.route('/master')
def master():
    return render_template('master.html')

@app.route('/player')
def player():
    return render_template('player.html', 
                           username=request.args.get('username'),)

@app.route('/dashboard')
def dashboard():
    # Render the dashboard page
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
