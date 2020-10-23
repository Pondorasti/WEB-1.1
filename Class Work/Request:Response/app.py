from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
    """Greets the user"""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return 'Penguins are cute!'

@app.route('/octocat')
def octocat():
    return '<img src="https://alexandruturcanu.com/images/faces/octocat.png">'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I like {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"This {noun} is {adjective}"

# @app.route('/multiply/<int:number1>/<int:number2>')
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1) * int(number2)}."
    return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<int:count>')
def sayntimes(word, count):
    result = ""
    for _ in range(count):
        result += word + " "
    return result[:-1]

@app.route('/reverse/<string>')
def reverse(string):
    return string[::-1]

@app.route('/strangecaps/<string>')
def strangecaps(string):
    result = ''
    for character in string:
        if randint(0, 1) == 0:
            result += character.upper()
        else:
            result += character.lower()
    return result 

@app.route('/dicegame')
def dicegame():
    dice_roll = randint(1, 6)
    if dice_roll == 6:
        return "You rolled a 6. You won!"
    return f"You rolled a {dice_roll}. You lost!"

if __name__ == "__main__":
    app.run(debug=True)