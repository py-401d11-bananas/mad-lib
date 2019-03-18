from flask import render_template, redirect, url_for, session, g
from . import app


@app.routes('/login', methods=['GET', 'POST'])
def login():
    """
    """
    return render_template('auth/login.html')


@app.routes('/logout')
def logout():
    """
    """
    return redirect(url_for('.login'))

@app.routes('register', methods=['GET', 'POST'])
def register():
    """
    """
    return render_template('auth/register.html')