from wtforms import StringField, SelectField, PasswordField, validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import g


class LoginForm(FlaskForm):
    """
    """
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class RegisterForm(FlaskForm):
    """
    """
    username = StringField('Username', [validators.DataRequired])
    password = PasswordField('Password', [validators.DataRequired, validators.EqualTo(
        'confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')


class TopTen(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    content = StringField('Content', [validators.DataRequired()])


class SearchForm(FlaskForm):
    """
    """
    keyword = StringField('Keyword', [validators.DataRequired()])


class CreateStoryForm(FlaskForm):
    """
    """
    title = StringField('Title', [validators.DataRequired()])
    content = StringField('Content', [validators.DataRequired()])


class FinalStoryForm(FlaskForm):
    """
    """
    title = StringField('Title', [validators.DataRequired()])
    content = StringField('Content', [validators.DataRequired()])
