from flask import render_template, redirect, url_for, session, request
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory, db
<<<<<<< HEAD
from .stories import *
from .utilities import send_prompts_to_form, convert_dict_to_model_instance
=======
from .utilities import *
>>>>>>> ea5e589a9ce197e1248ed42dbdaf65537a9b44be


@app.route('/',  methods=['GET', 'POST'])
def home():
    """
    """
    form = StorySelect()

    if form.validate_on_submit():
        story_id = form.data['stories']

        return redirect(url_for('.prompts', id=story_id))

    return render_template('home.html', form=form)


@app.route('/saved', methods=['GET', 'POST'])
def saved_stories():
    """
    """
    stories = UserStory.query.all()
    return render_template('saved.html', stories=stories)


@app.route('/story/<id>', methods=['GET', 'POST'])
def finished_story(id):
    """
    """

    form = FinalStoryForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user_story = UserStory(
                    title=form.data['title'],
                    content=form.data['content']
                )

                db.session.add(user_story)
                db.session.commit()
            except:
                return 'oh nooooooo!'
                
            return redirect(url_for('.saved_stories'))
        else:
            return str(form.errors)

    data = request.form.to_dict()

    keylist = []
    for key in data:
        keylist.append((int(key),data[key].upper()))


    story = PresetStory.query.filter_by(id=id).first()

    story_dict = {
        'title': story.title,
        'content': story.content,
        'prompts': story.prompts
    }

    story_array = array_from_story_string(story_dict)
    new_story_array = replace_words(story_array, keylist)
    new_story = string_from_array(new_story_array)

    form_context =  {
        'title': story_dict['title'],
        'content': new_story
    }

    form = FinalStoryForm(**form_context)

    return render_template('story.html', form=form, id=id, story=new_story, title=story_dict['title'])




@app.route('/prompts/<id>', methods=['GET', 'POST'])
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

    return render_template('prompts.html', stories_new=stories_new, id=id)


@app.route('/test_stories')
def test_stories():

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

    return 'hi'
