from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/df8b0a60d16b8292cfc4")
data = response.json()

posts_list = []
for post in data:
    posts_list.append(post)


@app.route("/")
def homepage():
    return render_template("index.html", all_posts=posts_list)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for blog_post in posts_list:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
