from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    text = ('  <h1>Guess a number between 0 and 9!</h1> '
            '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'
            '<iframe src="https://giphy.com/embed/9QulmfXapZhCyxpfBp" '
            'width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>')
    return text
random_num = randint(1, 9)
@app.route("/<int:guess>")
def checking(guess):
    if guess > random_num:
        return "<h1 style='color: green'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: blue'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)