from wftorms import StringField, SelectField, PasswordField
from wtfforms.validators import DataRequired
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
    password = PasswordField('Password'. [validatorsDataRequired, validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')


class TopTen(Flask):
    title = StringFields('Title', [validators.DataRequired()])
    description = StringFields('Description', [validators.DataRequired()])
    content = StringFields('Content', [validators.DataRequired()])

