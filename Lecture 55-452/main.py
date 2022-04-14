from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img " \
           "src='https://icatcare.org/app/uploads/2018/07/Helping-your-new-cat-or-kitten-settle-in-1.png', " \
           "width=400px>"


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"

    return wrapper


def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name + '12'}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
