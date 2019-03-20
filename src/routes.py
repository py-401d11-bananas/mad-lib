from flask import render_template, redirect, url_for
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory, db
from .sample import send_prompts_to_form


@app.route('/',  methods=['GET', 'POST'])
def home():
    """
    """
    form = StorySelect()

    if form.validate_on_submit():
        story_id = form.data['stories']

        return redirect(url_for('.prompts', id=story_id))

    return render_template('home.html', form=form)


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
        session['title'] = form.data['title']
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


@app.route('/prompts/<id>', methods=['GET', 'POST'])
def prompts(id):
    """
    """
    story = PresetStory.query.filter_by(id=id).first()
    form = PromptsForm()

    story_dict = {
        'title': story.title,
        'content': story.content,
        'prompts': story.prompts
    }

    stories_new = send_prompts_to_form(story_dict)

    return render_template('prompts.html', story=story, form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    """
    form = SearchForm()
    return render_template('results.html', form=form)


@app.route('/test_stories')
def test_stories():



    db.session.add(story1)
    db.session.add(story2)
    db.session.add(story3)
    db.session.commit()

    return 'hi'


@app.route('/get_stories')
def get_stories():
    stories = PresetStory.query.all()
    return stories[0].content
