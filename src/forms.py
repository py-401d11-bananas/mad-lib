from wtforms import StringField, SelectField, PasswordField, validators, RadioField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import g
from .models import PresetStory


class LoginForm(FlaskForm):
    """
    """
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class RegisterForm(FlaskForm):
    """
    """
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    # confirm = PasswordField('Confirm Password')
# , validators.EqualTo(
#         'confirm', message='Passwords must match')

class FinalStoryForm(FlaskForm):
    """
    """
    title = StringField('Title', [validators.DataRequired()])
    content = StringField('Content', [validators.DataRequired()])


class StorySelect(FlaskForm):
    """
    """
    stories = RadioField('Select Story', [validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stories.choices = [(str(s.id), s.title) for s in PresetStory.query.all()]


class PromptsForm(FlaskForm):
    pass
