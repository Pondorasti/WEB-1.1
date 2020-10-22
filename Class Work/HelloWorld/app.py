from flask import Flask, render_template, request
import helper



app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello, world!"

@app.route('/profile/<username>/<age>')
def profile(username, age):
    return f"Hey! My name is {username} and I am {age} years old"


@app.route('/file/<id>')
def file(id):
    content = render_template(f"file{id}.html")
    return content

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Authentificate user"
    else:
        return "Retrieving user"

if __name__ == '__main__':
    print("Hey brian")
    app.run(debug=True)


