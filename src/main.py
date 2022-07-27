from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="resources", template_folder="pages")


@app.route("/")
def base():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/socials")
def socials():
    return render_template("socials.html")
