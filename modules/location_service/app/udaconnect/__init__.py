import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(os.getenv("FLASK_ENV") or "test")

db.init_app(app)