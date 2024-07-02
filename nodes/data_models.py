# data_models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  # Add other character attributes as needed (e.g., description, skills)

class Location(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  # Add other location attributes as needed (e.g., description, connected locations)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  # Add other item attributes as needed (e.g., description, stats)

class Fact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable=False)
  # Add other fact attributes as needed (e.g., category, source)

