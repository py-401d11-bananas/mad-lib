"""
This Module contains all forms used in the application.

Classes
    LoginForm: Logs current users into their profile.
    RegisterForm: Registers a new user's unique username and password.
    FinalStoryForm: Allows a user to save their story.
    StorySelect: Provides options of stories for a user to choose.
    PromptsForm: Passes CSRF information with user responses to prompts.
"""

from .models import PresetStory
from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, validators, RadioField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    Logs current users into their profile.

    Attributes:
        username (str): Required. Must be unique.
        password (str): Required. A hashed version will be stored in the database.
    """

    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class RegisterForm(FlaskForm):
    """
    Registers a new user's unique username and password.

    Attributes:
        username (str): Required. Will compare to the database for verification.
        password (str): Required. A hashed version will compare to the database for verification.
    """
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    # confirm = PasswordField('Confirm Password')
# , validators.EqualTo(
#         'confirm', message='Passwords must match')

class FinalStoryForm(FlaskForm):
    """
    Allows a user to save their story.

    This form is pre-populated with the result story and hidden so users cannot adjust thier final story.

    Attributes:
        title (str): Required.
        content (str): Required.
    """

    title = StringField('Title', [validators.DataRequired()])
    content = StringField('Content', [validators.DataRequired()])


class StorySelect(FlaskForm):
    """
    Provides options of stories for a user to choose.

    Attributes:
        Stories (radio): A radio-selection style list of all pre-fabricated stories available.
    """
    stories = RadioField('Select Story', [validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stories.choices = [(str(s.id), s.title) for s in PresetStory.query.all()]


class PromptsForm(FlaskForm):
    """
    Passes CSRF information with user responses to prompts.

    This form does not have attributes, but allows for CSRF verification to be passed. The form used to collect user responses is dynamic to the number of allowable inputs unique to each story, and is rendered with HTML.
    """

    pass
