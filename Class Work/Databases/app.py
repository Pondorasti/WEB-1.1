from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

############################################################
# SETUP
############################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/plantsDatabase"
mongo = PyMongo(app)

plants_db = mongo.db.plants
harvests_db = mongo.db.harvests

############################################################
# ROUTES
############################################################

@app.route('/')
def plants_list():
    """Display the plants list page."""

    plants_data = plants_db.find({})

    context = {
        'plants': plants_data,
    }
    return render_template('plants_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    if request.method == 'POST':
        new_plant = {
            'name': request.form.get('plant_name'),
            'variety': request.form.get('variety'),
            'photo_url': request.form.get('photo'),
            'date_planted': request.form.get('date_planted')
        }

        plant_id = plants_db.insert_one(new_plant).inserted_id

        return redirect(url_for('detail', plant_id=plant_id))

    else:
        return render_template('create.html')

@app.route('/plant/<plant_id>')
def detail(plant_id):
    """Display the plant detail page & process data from the harvest form."""

    if not ObjectId.is_valid(plant_id):
        return render_template('404.html')
    
    plant_to_show = plants_db.find_one({'_id': ObjectId(plant_id)})
    harvests = harvests_db.find({'plant_id': plant_id})
    
    context = {
        'plant' : plant_to_show,
        'harvests': harvests
    }
    
    return render_template('detail.html', **context)
        

@app.route('/harvest/<plant_id>', methods=['POST'])
def harvest(plant_id):
    """
    Accepts a POST request with data for 1 harvest and inserts into database.
    """

    new_harvest = {
        'quantity': request.form.get('harvested_amount'), 
        'date': request.form.get('date_planted'),
        'plant_id': plant_id
    }

    harvests_db.insert_one(new_harvest)

    return redirect(url_for('detail', plant_id=plant_id))

@app.route('/edit/<plant_id>', methods=['GET', 'POST'])
def edit(plant_id):
    """Shows the edit page and accepts a POST request with edited data."""
    if request.method == 'POST':

        plants_db.update_one(
            {'_id'  : ObjectId(plant_id)},
            {'$set' : {
                'name': request.form.get('plant_name'),
                'variety': request.form.get('variety'),
                'photo_url': request.form.get('photo'),
                'date_planted': request.form.get('date_planted')
            }}
        )
        
        return redirect(url_for('detail', plant_id=plant_id))
    else:
        plant_to_show = plants_db.find_one({'_id' : ObjectId(plant_id)})
        print(plant_to_show)
        context = {
            'plant': plant_to_show
        }

        return render_template('edit.html', **context)

@app.route('/delete/<plant_id>', methods=['POST'])
def delete(plant_id):
    
    plants_db.delete_one({'_id' : ObjectId(plant_id)})
    harvests_db.delete_many({'plant_id' : plant_id})

    return redirect(url_for('plants_list'))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=False)