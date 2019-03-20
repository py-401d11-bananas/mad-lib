from ..models import User, UserStory


class TestUserModel:
    """

    """
    def test_user_create(self, user):
        assert user.id > 0

    def test_user_username(self, user):
        assert user.username == 'potato'

    def test_user_password(self, user):
        assert user.password == 'secret'


class TestUserStoriesModel:
    """

    """
    def test_stories_empty(self, db_session):
        stories = UserStory.query.all()
        assert len(stories) == 0

    def test_create_story(self, user_story):
        assert UserStory.id > 0

    def test_story_title(self, user_story):
        assert user_story.title == 'Story Title'

    def test_story_content(self, user_story):
        assert user_story.content == 'This is the actual story'

    def test_story_user_id(self, user_story):
        assert user_story.user_id == 1
