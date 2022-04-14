from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 9)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif', width=400px>"


@app.route("/<int:guess>")
def cold_checker(guess):
    if guess > random_number:
        return "<h1 style='color:red;'>Your guess is too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color:blue;'>Your guess is too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    else:
        return "<h1 style='color:green;'>You found the number!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
