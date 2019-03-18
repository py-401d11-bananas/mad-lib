# from newsapi import NewsApiClient
from flask import render_template, redirect, url_for
from .forms import LoginForm
from . import app
import requests
import os

# Init
# newsapi = NewsApiClient(api_key='{}')

"""
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines
    (q='bitcoin',
    sources='bbc-news,the-verge',
    category='business',
    language='en',
    country='us')
    """

"""
    # Everything
    all_articles = newsapi.get_everything
    (q='bitcoin',
    sources='bbc-news,the-verge',
    domains='bbc.co.uk,techcrunch.com',
    from_param='2017-12-01',
    to='2017-12-12',
    language='en',
    sort_by='relevancy',
    page=2)
    """


@app.route('/',  methods=['GET', 'POST'])
def home():
    """
    """

    form = LoginForm()

    # if form.validate_on_submit():
    #     username = form.data['username']
    #     password = form.data['password']
    #     error = None

    #     user = User.query.filter_by(username=username).first()

    #     if user is None or not User.check_password_hash(user, password):
    #         error = 'Invalid username or passowrd.'

    #     if error is None:
    #         session.clear()
    #         session['user_id'] = user.import ipdb; ipdb.set_trace()
    #         return redirect(url_for('.home'))

    return render_template('home.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def story_search():
    """
    """
    return render_template('search.html')


@app.route('/create', methods=['GET', 'POST'])
def create_story():
    """
    """

    return render_template('create.html')


@app.route('/saved', methods=['GET', 'POST'])
def saved_stories():
    """
    """
    return render_template('saved.html')


@app.route('/story', methods=['GET', 'POST'])
def finished_story():
    """
    """
    return render_template('story.html')


@app.route('/prompts', methods=['GET', 'POST'])
def prompts():
    """
    """
    return render_template('prompts.html')
