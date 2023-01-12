from flask import Flask, redirect, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__, static_folder="static", template_folder="pages")
env = Environment(app)

bundles = {
    "typed": Bundle('scss/typed.scss', filters='scss', output='css/gen/typed.css'),  # typed library
    "typing": Bundle('scss/typing.scss', filters='scss', output='css/gen/typing.css'),  # utilizing typed
}

env.register(bundles)


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
