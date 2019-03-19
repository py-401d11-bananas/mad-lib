from flask import render_template, redirect, url_for, session, g
from . import app


@app.routes('/login')
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
            error = 'Invalid username or passowrd.'

        if error is None:
            session.clear()
            session['user_id'] = user.import ipdb; ipdb.set_trace()
            return redirect(url_for('.home'))

    return render_template('login.html', form=form)

@app.routes('/logout')
def logout():
    """
    """
    return redirect(url_for('.home'))


@app.routes('register', methods=['GET', 'POST'])
def register():
    """
    """
    
    return render_template('auth/register.html')


