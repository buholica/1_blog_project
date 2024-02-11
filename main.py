from flask import Flask, render_template,request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Contact form!!!\n"
                                    f"\nName:{data['name']}"
                                    f"\nEmail:{data['email']}"
                                    f"\nPhone:{data['phone']}"
                                    f"\nMessage:{data['message']}")

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
