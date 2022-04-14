from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def ageify_genderize(name):
    response_gender = requests.get(f"https://api.genderize.io?name={name}").json()
    response_age = requests.get(f"https://api.agify.io?name={name}").json()
    gender = response_gender["gender"]
    age = response_age["age"]
    return render_template("ageify_genderize.html", name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/dfe1d1c90d5a68f60ab6"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)
