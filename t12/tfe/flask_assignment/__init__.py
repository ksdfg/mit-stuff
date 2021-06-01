from os.path import join, dirname, realpath

from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    "meow",
    template_folder=join(dirname(realpath(__file__)), "templates"),
    static_folder=join(dirname(realpath(__file__)), "static"),
)
app.config["SQLALCHEMY_DATABASE_URI"] = config("flask_db_uri")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from .models import *
from .routes import *


@app.get("/")
def hello_world() -> str:
    return render_template("base.html")
