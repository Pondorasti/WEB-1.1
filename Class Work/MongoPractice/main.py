from flask import Flask, request, redirect, render_template, url_for
from pymongo import MongoClient
# from bson.objectid import ObjectId

####################################################
# SETUP
####################################################

app = Flask(__name__)

# Define a new client
client = MongoClient('mongodb+srv://replit:makeschool@cluster0.idqxn.mongodb.net/test?retryWrites=true&w=majority')

# Get the database (database name by default is "test")
db = client.test

fruits_collection = db.fruits5

####################################################
# ROUTES
####################################################

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/show_all_fruits')
def show_all_fruits():
  """Show all fruits in the database."""

  fruits = fruits_collection.find({})
  for fruit in fruits:
    print(fruit)

  context = {
    'list_of_fruits': fruits_collection.find({})
  }

  return render_template('show_fruits.html', **context)


@app.route('/fruits_search')
def fruits_search():
  """Show all fruits of a certain name in the database."""

  context = {
    # TODO: Get all fruits with the specified name by calling `find()`
    'list_of_fruits': fruits_collection.find({"name" : request.form.get("fruit_name")})
  }

  return render_template('show_fruits.html', **context)


@app.route('/add_fruit', methods=['POST'])
def add_fruit():
  """Add a new fruit to the database."""

  fruit = {
    "name" : request.form.get("fruit_name"),
    "price" : request.form.get("price")
  }
  # TODO: Return an error message if the fruit doesn't have a name or a price

  fruits_collection.insert_one(fruit)
  # TODO: Return a success message
  return "Not Yet Implemented!"


@app.route('/update_fruit', methods=['POST'])
def update_fruit():
  """Update an existing fruit in the database."""
  # TODO: Return an error message if the fruit doesn't have a name or a price

  # TODO: Update the fruit to have the new price using `update_one()`

  # TODO: Return a success message
  return "Not Yet Implemented!"


@app.route('/delete_fruit', methods=['POST'])
def delete_fruit():
  """Delete an existing fruit from the database."""
  # TODO: Return an error message if the fruit doesn't have a name

  # TODO: Delete the fruit from the database

  # TODO: Return a success message
  return "Not Yet Implemented!"

app.run('0.0.0.0', debug=True)