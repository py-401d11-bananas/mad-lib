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
    # user_story = db.relationship('UserStory', backref='user_story', lazy=True)

    def __repr__(self):
        return '<User: {}>'.format(self.email)

    def __init__(self, email, password):
        self.email = email
        self.password = sha256_crypt.hash(password)


class PresetStory(db.Model):
    __tablename__ = 'preset_story'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.Text, unique=True)
    prompts = db.Column(db.Text)

    def __repr__(self):
        return '<Preset Story: {}>'.format(self.title)


class UserStory(db.Model):
    __tablename__ = 'user_stories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.Text, unique=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    # user_id = db.Column(db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return '<User Story: {}>'.format(self.title)


story1 = PresetStory(title='The Boy Who Cried Wolf', content="""Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, he shouted, "Wolf! Wolf! The sheep are being chased by the wolf!" The villagers came running to help the boy and save the sheep. They found nothing and the boy just laughed looking at their angry faces. "Don't cry 'wolf' when there's no wolf boy!", they said angrily and left. The boy just laughed at them. After a while, he got bored and cried 'wolf!' again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, "Wolf! Please help! The wolf is chasing the sheep. Help!" But this time, no one turned up to help. By evening, when the boy didn't return home, the villagers wondered what happened to him and went up the hill. The boy sat on the hill weeping. "Why didn't you come when I called out that there was a wolf?" he asked angrily. "The flock is scattered now", he said. An old villager approached him and said, "People won't believe liars even when they tell the truth. We'll look for your sheep tomorrow morning. Let's go home now".""", prompts="""*|*|*|*|*|Past Tense Verb|*|Profession|*|*|*|*|Verb Ending in -ing|*|*|*|Animal Plural|*|*|*|*|Verb|*|*|*|*|*|*|Animal Plural|*|*|Past Tense Verb|*|*|*|*|Plural Noun|*|Verb Ending in -ing|*|*|*|*|*|Verb|*|*|*|Past Tense Verb|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|Adjective|*|*|Verb|*|*|*|*|Aniimal|*|*|Past Tense Verb|Adverb|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Verb Ending in -ing|*|Plural Noun|*|*|*|*|Adjective|Plural Noun|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|*|*|*,|*|Past Tense Verb|*|Adjective|Animal|*|Past Tense Verb|*|*|*|*|*|Animal|*|Verb Ending in -ing|*|*|*|*|*|*,|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Verb|*|*|Plural Noun|Past Tense Verb|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Noun|*|*|*|*|Verb|*|*|Past Tense Verb|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Adjective Beginning with a Vowel|Noun|Past Tense Verb|*|*|*|*|*|*|Plural Noun|*|*|*|Verb|*|*|*|Verb|*|*|Animal Plural|*|*|*|*|*|*""")

story2 = PresetStory(title='The Golden Egg', content="""Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs. The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, "Why should I take just one egg a day? Why can't I take all of them at once and make a lot of money?" The foolish farmer's wife also agreed and decided to cut the goose's stomach for the eggs. As soon as they killed the bird and opened the goose's stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!""", prompts="""*|*|*|*,|*|Profession|*|*|Animal|*|Past Tense Verb|*|Adjective|Noun|*|*|*|Noun|Past Tense Verb|*|Plural Noun|*|*|Profession|*|*|*|*|*|*|*|*|Profession|*|*|*|*|*|*|*|*|*|*|*|*|*|Profession|*|*|Noun Beginning with a Vowel|*|*|*|*|*|Verb|*|*|Noun|*|*|*|*|*|Verb|*|*|*|*|*|*|*|*|*|*|*|*|Adjective|*|*|*|Past Tense Verb|*|Past Tense Verb|*|Verb|*|*|Body Part|*|*|*|*|*|*|*|Past Tense Verb|*|Animal|*|Past Tense Verb|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|Verb Ending in -ing|*|Adjective|*|*|*|*|Adjective|*""")
