from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="resources", template_folder="pages")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/github")
def github():
    return redirect("https://github.com/baronkobama", code=302)


@app.route("/discord")
def discord():
    return redirect("https://discord.com/users/335241734088949760", code=302)
