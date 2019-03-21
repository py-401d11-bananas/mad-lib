from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app
from passlib.hash import sha256_crypt

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    user_story = db.relationship('UserStory', backref='user_story', lazy=True)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def __init__(self, username, password):
        self.username = username
        self.password = sha256_crypt.hash(password)

    @classmethod
    def check_password_hash(cls, user, password):
        if user is not None:
            if sha256_crypt.verify(password, user.password):
                return True

        return False


class PresetStory(db.Model):
    __tablename__ = 'preset_story'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.Text)
    prompts = db.Column(db.Text)

    def __repr__(self):
        return '<Preset Story: {}>'.format(self.title)


class UserStory(db.Model):
    __tablename__ = 'user_stories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.now())
    user_id = db.Column(db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return '<User Story: {}>'.format(self.title)
