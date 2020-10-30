from flask import Flask, request, render_template
import random
import operator

app = Flask(__name__)
ops = {
    'add' : operator.add,
    'subtract' : operator.sub,
    'multiply' : operator.mul,
    'divide' : operator.truediv
}

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""

    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    flavor = request.args.get('flavor')
    toppings = request.args.get('toppings')

    return render_template('froyo_results.html', flavor=flavor, toppings=toppings)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""

    return render_template('favorites_form.html')

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    context = {
        'color' : request.args.get('color'),
        'animal' : request.args.get('animal'),
        'city' : request.args.get('city')
    }

    return render_template('favorites_results.html', **context)

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""

    return render_template('message_form.html')

@app.route('/message_results', methods=['POST', 'GET'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    encrypted_message = sort_letters(message)

    return render_template('message_results.html', message=encrypted_message)

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = int(request.args.get('operand1'))
    operand2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')

    result = ops[operation](operand1, operand2)

    context = {
        'operand1'  : operand1,
        'operand2'  : operand2,
        'operation' : operation,
        'result'    : result 
    }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    name = request.args.get('users_name')
    should_show_compliments = request.args.get('wants_compliments')
    number_of_compliments = request.args.get('num_compliments')

    compliments = None
    if should_show_compliments == 'yes' and number_of_compliments.isdigit():
        compliments = random.sample(list_of_compliments, int(number_of_compliments))

    context = {
        'name' : name,
        'compliments' : compliments
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
