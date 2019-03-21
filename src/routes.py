"""
This Module contains base routes.

Route Functions
    home: Renders the home page, where a user can choose a story.
    prompts: Renders a page where the user fills in parts of speech prompts.
    finished_story: Allows the user to review thier new story with the option to save it.
    saved_stories: Allows the user to view all thier saved stories.
    seed_stories: Used to plant pre-faricated stories in the database.
"""

from . import app
from .auth import login_required, login
from .forms import *
from .models import PresetStory, UserStory, db
from .stories import *
from .utilities import *
from flask import render_template, redirect, url_for, session, request, g, flash
import os
import requests
from sqlalchemy.exc import DBAPIError, InvalidRequestError


@app.route('/',  methods=['GET', 'POST'])
def home():
    """
    Renders the home page, where a user can choose from a selection of stories.

    Returns
        Home Page: Renders if user is logged in.
        Login Page: Redirects if user is not logged in.
        Prompts Page: Redirects to the prompts page if the user selects a story.
    """

    if g.user:

        form = StorySelect()

        if form.validate_on_submit():
            story_id = form.data['stories']

            return redirect(url_for('.prompts', id=story_id))

        return render_template('home.html', form=form)

    return redirect(url_for('.login'))


@app.route('/prompts/<id>', methods=['GET'])
@login_required
def prompts(id):
    """
    Renders a page where the user fills in parts of speech prompts.

    Args
        id: The id of the selected story, passed with the redirect from the home page.

    Returns
        Story Page: Redirects to the story page, passing the user's inputs.
        
    """

    story = PresetStory.query.filter_by(id=id).first()

    story_dict = {
        'title': story.title,
        'content': story.content,
        'prompts': story.prompts
    }

    stories_new = send_prompts_to_form(story_dict)

    return render_template('prompts.html', stories_new=stories_new, id=id, form=PromptsForm())


@app.route('/story/<id>', methods=['GET', 'POST'])
@login_required
def finished_story(id):
    """
    Allows the user to review thier new story with the option to save it.

    Args
        id: The id of the selected story, passed with the redirect from the prompts page.

    Returns
        Prompts Page: Redirects user to the prompts page if they arrive at the story page without having entered prompts.
        Saved Stories Page: Renders the Saved Stories page.
    """
    if request.method == 'GET':
        return redirect(url_for('.prompts', id=id))

    data = request.form.to_dict()
    keylist = []
    for key in data:
        keylist.append((int(key), data[key].upper()))

    story = PresetStory.query.filter_by(id=id).first()

    story_dict = {
        'title': story.title,
        'content': story.content,
        'prompts': story.prompts
    }

    story_array = array_from_story_string(story_dict)
    new_story_array = replace_words(story_array, keylist)
    new_story = string_from_array(new_story_array)

    form_context = {
        'title': story_dict['title'],
        'content': new_story
    }

    form = FinalStoryForm(**form_context)

    return render_template('story.html', form=form, id=id, story=new_story, title=story_dict['title'])


@app.route('/saved', methods=['GET', 'POST'])
@login_required
def saved_stories():
    """
    Allows the user to view all thier saved stories.

    Returns
        Saved Stories Page: Renders the saved stories page.
        Home Page: If there is an error, the user is redirected to the home page.

    Exceptions
        DBAPIError: Failure of saving to a database.
        InvalidRequestError: Runtime state or other SQLAlchemy errors.
    """
    form = FinalStoryForm()

    if form.validate_on_submit():
        try:
            user_story = UserStory(
                title=form.data['title'],
                content=form.data['content'],
                user_id=g.user.id
            )

            db.session.add(user_story)
            db.session.commit()

        except (DBAPIError, InvalidRequestError):
            flash('I AM GROOT?')
            return render_template('/home.html')

        return redirect(url_for('.saved_stories'))

    stories = UserStory.query.filter(UserStory.user_id == g.user.id).all()
    return render_template('saved.html', stories=stories)


@app.route('/test_stories')
def seed_stories():
    """
    Plants pre-faricated stories in the database.

    Used for the developers to add additional pre-fabricated stories to the database. Returns a message of successful planting.
    """

    story1 = convert_dict_to_model_instance(story_one)
    story2 = convert_dict_to_model_instance(story_two)
    story3 = convert_dict_to_model_instance(story_three)
    story4 = convert_dict_to_model_instance(story_four)
    story5 = convert_dict_to_model_instance(story_five)

    db.session.add(story1)
    db.session.add(story2)
    db.session.add(story3)
    db.session.add(story4)
    db.session.add(story5)
    db.session.commit()

    return 'Stories added to database!'
