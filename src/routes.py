# from newsapi import NewsApiClient
from flask import render_template, redirect, url_for
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory

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
    stories = PresetStory.query.all()
    return render_template('home.html', stories=stories)


@app.route('/search', methods=['GET', 'POST'])
def story_search():
    """
    """
    form = SearchForm()

    return render_template('search.html', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create_story():
    """
    """
    form = CreateStoryForm()

    if form.validate_on_submit():
        session['title']= form.data['title']
        session['content'] = form.data['content']

        return redirect(url_for('.prompts'))

    return render_template('create.html', form=form)


@app.route('/saved', methods=['GET', 'POST'])
def saved_stories():
    """
    """
    stories = UserStory.query.all()
    return render_template('saved.html')


@app.route('/story', methods=['GET', 'POST'])
def finished_story():
    """
    """
    form = FinalStoryForm()
    return render_template('story.html', form=form)


@app.route('/prompts', methods=['GET', 'POST'])
def prompts():
    """
    """
    form = PromptsForm()
    return render_template('prompts.html', form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    """
    form = SearchForm()
    return render_template('results.html', form=form)
