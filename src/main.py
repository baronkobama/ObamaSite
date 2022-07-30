from flask import Flask, render_template

app = Flask(__name__, static_folder="resources", template_folder="pages")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")
