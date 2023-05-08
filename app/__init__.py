from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import models, views


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
db.create_all()
