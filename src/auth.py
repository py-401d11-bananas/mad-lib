from flask import render_template, redirect, url_for, session, g, flash, abort
import functools
from . import app
from .forms import LoginForm, RegisterForm
from .models import db, User


def login_required(view):
    """

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

    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    """
    form = LoginForm()

    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        error = None

        user = User.query.filter_by(username=username).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Invalid username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('.home'))

    return render_template('auth/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
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
    """
    session.clear()
    flash('See you again soon!')
    return redirect(url_for('.login'))
