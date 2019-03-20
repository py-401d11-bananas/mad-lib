from flask import render_template, redirect, url_for, session, request
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory, db
from .utilities import *


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

    return render_template('story.html', form=form, story=new_story, title=story_dict['title'])


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

    story1 = PresetStory(title='The Boy Who Cried Wolf', content="""Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, he shouted, "Wolf! Wolf! The sheep are being chased by the wolf!" The villagers came running to help the boy and save the sheep. They found nothing and the boy just laughed looking at their angry faces. "Don't cry 'wolf' when there's no wolf boy!", they said angrily and left. The boy just laughed at them. After a while, he got bored and cried 'wolf!' again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, "Wolf! Please help! The wolf is chasing the sheep. Help!" But this time, no one turned up to help. By evening, when the boy didn't return home, the villagers wondered what happened to him and went up the hill. The boy sat on the hill weeping. "Why didn't you come when I called out that there was a wolf?" he asked angrily. "The flock is scattered now", he said. An old villager approached him and said, "People won't believe liars even when they tell the truth. We'll look for your sheep tomorrow morning. Let's go home now".""", prompts="""*|*|*|*|*|Past Tense Verb|*|Profession|*|*|*|*|Verb Ending in -ing|*|*|*|Animal Plural|*|*|*|*|Verb|*|*|*|*|*|*|Animal Plural|*|*|Past Tense Verb|*|*|*|*|Plural Noun|*|Verb Ending in -ing|*|*|*|*|*|Verb|*|*|*|Past Tense Verb|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|Adjective|*|*|Verb|*|*|*|*|Aniimal|*|*|Past Tense Verb|Adverb|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Verb Ending in -ing|*|Plural Noun|*|*|*|*|Adjective|Plural Noun|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|*|*|*,|*|Past Tense Verb|*|Adjective|Animal|*|Past Tense Verb|*|*|*|*|*|Animal|*|Verb Ending in -ing|*|*|*|*|*|*,|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Verb|*|*|Plural Noun|Past Tense Verb|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Noun|*|*|*|*|Verb|*|*|Past Tense Verb|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Adjective Beginning with a Vowel|Noun|Past Tense Verb|*|*|*|*|*|*|Plural Noun|*|*|*|Verb|*|*|*|Verb|*|*|Animal Plural|*|*|*|*|*|*""")

    story2 = PresetStory(title='The Golden Egg', content="""Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs. The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, "Why should I take just one egg a day? Why can't I take all of them at once and make a lot of money?" The foolish farmer's wife also agreed and decided to cut the goose's stomach for the eggs. As soon as they killed the bird and opened the goose's stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!""", prompts="""*|*|*|*,|*|Profession|*|*|Animal|*|Past Tense Verb|*|Adjective|Noun|*|*|*|Noun|Past Tense Verb|*|Plural Noun|*|*|Profession|*|*|*|*|*|*|*|*|Profession|*|*|*|*|*|*|*|*|*|*|*|*|*|Profession|*|*|Noun Beginning with a Vowel|*|*|*|*|*|Verb|*|*|Noun|*|*|*|*|*|Verb|*|*|*|*|*|*|*|*|*|*|*|*|Adjective|*|*|*|Past Tense Verb|*|Past Tense Verb|*|Verb|*|*|Body Part|*|*|*|*|*|*|*|Past Tense Verb|*|Animal|*|Past Tense Verb|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|Verb Ending in -ing|*|Adjective|*|*|*|*|Adjective|*""")

    story3 = PresetStory(title='The Wet Pants', content="""A nine-year-old boy was sitting at his desk in class, when suddenly, his pants felt wet, and there was a puddle at his feet. His heart almost skipped a beat, as he got worried that his classmates would see that and make fun of him. He quickly wanted to do something, and saw the teacher and his classmate Susie walking towards him. Susie was carrying a bowl of goldfish. As they came closer, the boy thought that the teacher noticed his wet pants, and suddenly Susie trips and drops the fishbowl in his lap. While thanking God for helping him, he pretends to get angry with Susie and yells at her. Everyone in the class thinks it is Susie’s fault that the boy’s pants got wet. The teacher helps the boy change into dry clothes, and the class continues. Later that evening, the boy asks Susie, “You did that on purpose, didn’t you?” “I wet my pants once too”, whispers Susie.""", prompts="""*|*|*|*|Verb Ending in -ing|*|*|Noun|*|*|*|*|*|Plural Noun|*|*|*|*|*|*|Noun|*|*|*|*|Body Part|*|Past Tense Verb|*|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|*|*|*|*|*|Adverb|Past Tense Verb|*|*|*|*|Past Tense Verb|*|Profession|*|*|Noun|*|Verb Ending in -ing|*|*|*|*|Verb Ending in -ing|*|Noun|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Profession|Past Tense Verb|*|Adjective|*|*|Adverb|*|Verb Ending in -s|*|Verb Ending in -s|*|Noun|*|*|*|*|Verb Ending in -ing|*|*|Verbing Ending in -ing|*|*|Verb Ending in -s|*|*|*|*|*|*|Verb Ending in -s|*|*|*|*|*|Noun|Verb Ending in -s|*|*|*|*|*|*|*|Plural Noun|*|*|*|Profession|Verb Ending in -s|*|*|Verb|*|Adjective|*|*|*|Noun|*|*|*|*|*|*|Verb Ending in -s|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|Plural Noun|*|*|Verb Ending in -s|*""")

    db.session.add(story1)
    db.session.add(story2)
    db.session.add(story3)
    db.session.commit()

    return 'hi'
