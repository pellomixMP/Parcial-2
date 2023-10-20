from flask import Flask
from .extensions import db
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


















