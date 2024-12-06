import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flaskr import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=dt.datetime.now(dt.UTC))
    image = db.Column(db.String(150), nullable=True)  # Путь к изображению
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
