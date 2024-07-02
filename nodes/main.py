import os
from flask import Flask, render_template, request, redirect, url_for
from data_models import db, Character, Location, Item, Fact

# Define the absolute path to the database file
db_path = os.path.join(os.getcwd(), 'databases', 'data.db')

app = Flask(__name__)
# Configure the Flask app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db.init_app(app)

def create_tables():
    try:
        with app.app_context():
            db.create_all()
    except FileNotFoundError:
        print("Error: Database file not found!")

@app.route('/')
def index():
  # You can add logic here to retrieve data from your models or prepare information for the template
  return render_template('index.html')

@app.route('/add_node')
def add_node():
  # You can pass any data needed to the template here (e.g., node types)
  return render_template('add_node.html')


if __name__ == '__main__':
  app.run(debug=True)
