from ..models import User, UserStory, PresetStory
from ..utilities import convert_dict_to_model_instance
from ..stories import *
import pytest


class TestUserModel:
    """

    """
    # @pytest.mark.skip
    def test_user_create(self, user):
        assert user.id > 0

    def test_user_username(self, user):
        assert user.username == 'potato'

    def test_user_password(self, user):
        assert User.check_password_hash(user, 'secret')


class TestUserStoriesModel:
    """

    """
    def test_stories_empty(self, db_session):
        stories = UserStory.query.all()
        assert len(stories) == 0

    def test_create_story(self, user_story):
        assert user_story.id > 0

    def test_story_title(self, user_story):
        assert user_story.title == 'Story Title'

    def test_story_content(self, user_story):
        assert user_story.content == 'This is the actual story'

    def test_story_user_id(self, user_story):
        assert user_story.user_id == 1


class TestPresetStoriesModel:
    """

    """
    def test_dict_to_db_one_entry(self, preset_story):
        stories = PresetStory.query.all()
        assert preset_story.title == story_one['title']
        assert len(stories) == 1
        assert stories[0].content == story_one['content']
