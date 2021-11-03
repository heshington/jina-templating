from flask import Flask, render_template
from datetime import date
import requests
app = Flask(__name__)


@app.route('/guess/<name>')
def guess_user(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    age_data = age_response.json()
    age = age_data['age']
    user_gender = gender_data['gender']
    return render_template("gussed.html", gussed_age=age, name= name, user_gender=user_gender )

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    blogs = requests.get(blog_url)
    all_posts = blogs.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


