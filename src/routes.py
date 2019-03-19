# from newsapi import NewsApiClient
from flask import render_template, redirect, url_for
from .forms import *
from . import app
import requests
import os
from .models import PresetStory, UserStory, db

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
    form = StorySelect()

    if form.validate_on_submit():
        story = PresetStory.query.filter_by(id=form.data['stories'])

        return redirect(url_for('.prompts'))

    stories = PresetStory.query.all()
    return render_template('home.html', stories=stories, form=form)


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


@app.route('/prompts', methods=['GET', 'POST'])
def prompts():
    """
    """
    import pdb; pdb.set_trace()
    form = PromptsForm()
    return render_template('prompts.html', form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    """
    form = SearchForm()
    return render_template('results.html', form=form)


@app.route('/test_stories')
def test_stories():
    story1 = PresetStory(title='The Boy Who Cried Wolf', content="""Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, he shouted, "Wolf! Wolf! The sheep are being chased by the wolf!" The villagers came running to help the boy and save the sheep. They found nothing and the boy just laughed looking at their angry faces. "Don't cry 'wolf' when there's no wolf boy!", they said angrily and left. The boy just laughed at them. After a while, he got bored and cried 'wolf!' again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, "Wolf! Please help! The wolf is chasing the sheep. Help!" But this time, no one turned up to help. By evening, when the boy didn't return home, the villagers wondered what happened to him and went up the hill. The boy sat on the hill weeping. "Why didn't you come when I called out that there was a wolf?" he asked angrily. "The flock is scattered now", he said. An old villager approached him and said, "People won't believe liars even when they tell the truth. We'll look for your sheep tomorrow morning. Let's go home now".""", prompts="""*|*|*|*|*|Past Tense Verb|*|Profession|*|*|*|*|Verb Ending in -ing|*|*|*|Animal Plural|*|*|*|*|Verb|*|*|*|*|*|*|Animal Plural|*|*|Past Tense Verb|*|*|*|*|Plural Noun|*|Verb Ending in -ing|*|*|*|*|*|Verb|*|*|*|Past Tense Verb|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|Adjective|*|*|Verb|*|*|*|*|Aniimal|*|*|Past Tense Verb|Adverb|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Verb Ending in -ing|*|Plural Noun|*|*|*|*|Adjective|Plural Noun|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|Verb Ending in -ing|*|*|*|*|*,|*|Past Tense Verb|*|Adjective|Animal|*|Past Tense Verb|*|*|*|*|*|Animal|*|Verb Ending in -ing|*|*|*|*|*|*,|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Verb|*|*|Plural Noun|Past Tense Verb|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Past Tense Verb|*|*|Noun|*|*|*|*|Verb|*|*|Past Tense Verb|*|*|*|*|*|*|*|Past Tense Verb|*|*|*|*|*|*|*|*|*|Adjective Beginning with a Vowel|Noun|Past Tense Verb|*|*|*|*|*|*|Plural Noun|*|*|*|Verb|*|*|*|Verb|*|*|Animal Plural|*|*|*|*|*|*""")
    story2 = PresetStory(title='The Golden Egg', content="""Once upon a time, a farmer had a goose that laid a golden egg every day. The egg provided enough money for the farmer and his wife for their day-to-day needs. The farmer and his wife were happy for a long time. But one day, the farmer got an idea and thought, "Why should I take just one egg a day? Why can't I take all of them at once and make a lot of money?" The foolish farmer's wife also agreed and decided to cut the goose's stomach for the eggs. As soon as they killed the bird and opened the goose's stomach, to find nothing but guts and blood. The farmer, realizing his foolish mistake, cries over the lost resource!""", prompts="""*|*|*|*,|*|Profession|*|*|Animal|*|Past Tense Verb|*|Adjective|Noun|*|*|*|Noun|Past Tense Verb|*|Plural Noun|*|*|Profession|*|*|*|*|*|*|*|*|Profession|*|*|*|*|*|*|*|*|*|*|*|*|*|Profession|*|*|Noun Beginning with a Vowel|*|*|*|*|*|Verb|*|*|Noun|*|*|*|*|*|Verb|*|*|*|*|*|*|*|*|*|*|*|*|Adjective|*|*|*|Past Tense Verb|*|Past Tense Verb|*|Verb|*|*|Body Part|*|*|*|*|*|*|*|Past Tense Verb|*|Animal|*|Past Tense Verb|*|*|*|*|*|*|*|Plural Noun|*|*|*|*|Verb Ending in -ing|*|Adjective|*|*|*|*|Adjective|*""")
    
    db.session.add(story1)
    db.session.add(story2)
    db.session.commit()

    return 'hi'


@app.route('/get_stories')
def get_stories():
    stories = PresetStory.query.all()
    return stories[0].content