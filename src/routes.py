from flask import render_template, redirect, url_for, session, request, g, flash
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory, db
from .stories import *
from .utilities import *
from .auth import login_required, login
from sqlalchemy.exc import DBAPIError, InvalidRequestError


@app.route('/',  methods=['GET', 'POST'])
def home():
    """
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
    """
    if request.method == 'GET':
        return redirect(url_for('.prompts', id=id))

    data = request.form.to_dict()
    keylist = []
    for key in data:
        keylist.append((int(key), '*' + data[key]))

    story = PresetStory.query.filter_by(id=id).first()

    story_dict = {
        'title': story.title,
        'content': story.content,
        'prompts': story.prompts
    }

    story_array = array_from_story_string(story_dict['content'])
    new_story_array = replace_words(story_array, keylist)
    new_story = string_from_array(new_story_array)

    form_context = {
        'title': story_dict['title'],
        'content': new_story
    }

    form = FinalStoryForm(**form_context)

    return render_template(
        'story.html',
        form=form,
        id=id,
        new_story=new_story,
        title=story_dict['title'],
        array_from_story_string=array_from_story_string
    )


@app.route('/saved', methods=['GET', 'POST'])
@login_required
def saved_stories():
    """
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

    return 'stories added to database!'
