"""
This Module contains functions related to user authorization and authentication.

Classes
    Users: Database containing user information.
    LoginForm: Form for current users to login to their unique profile.
    RegisterForm: Form for new users to create a unique login.

Functions
    login_required: Creates a function wrapper that restrict access to base routes to logged-in users only.
    load_logged_in_user: Assigns a user id to a login session.
    login: Renders a login form and validates entered username and password against the User database.
    register: Renders a register form and commits a new username and password information to the User database.
    logout: Clears the user id from the current session and redirects to the home page.
"""

from . import app
from .forms import LoginForm, RegisterForm
from .models import db, User
from flask import render_template, redirect, url_for, session, g, flash, abort
import functools


def login_required(view):
    """
    Creates a function wrapper that restrict access to base routes to logged-in users only.

    Exceptions:
        404 - Page Not Found: Directs users who are not logged in to a 404 Page Not Found.
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(404)

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """
    Assigns a user id to a login session.

    Retrieves the user id from the database if the user exists and assigns the value to the current user.
    """

    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Allows a user to login.

    Renders a login form and validates entered username and password against the User database. Notifies the user if invalid information is entered.

    Returns
        Login Page: Renders the login page.
        Home Page: Renders the 'logged in' view of the home page.
    """

    form = LoginForm()

    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        error = None

        user = User.query.filter_by(username=username).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Invalid username or password.'
            flash(error)

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('.home'))

    return render_template('auth/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Allows a new user to register.

    Returns
        Register Page: Renders the registration page.
        Login Page: Redirects to the login page upon validation of new user information entered on the register form, or redirects with a notification that an entered username already exists in the database.
    """

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        # confirm = form.data['confirm']
        error = None

        if not username or not password:
            error = 'Invalid Username or Password'

        if User.query.filter_by(username=username).first() is not None:
            flash('{} has already been registered!'.format(username))

            return redirect(url_for('.login'))

        if error is None:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()

            flash('Registration complete! Please log in.')

            return redirect(url_for('.login'))

        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    Logs a user out of their profile.

    Clears the user id from the current session and redirects to the home page.

    Returns
        Login Page: Redirects to login page.
    """
    session.clear()
    flash('See you again soon!')
    return redirect(url_for('.login'))
