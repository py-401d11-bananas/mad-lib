from ..models import User, PresetStory, UserStory
from ..models import db as _db
from .. import app as _app
import pytest
import os


@pytest.fixture()
def app(request):
    """

    """
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False,
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture()
def db(app, request):
    """

    """
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture()
def db_session(db, request):
    """

    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def client(app, db, db_session):
    """

    """
    client - app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture()
def user(db_session):
    """

    """
    user = User(username='potato', password='secret')

    db_session.add(user)
    db_session.commit()

    return user


@pytest.fixture()
def authenticated_client(client, user):
    """

    """
    client.post(
        '/login',
        data={'username': user.username, 'password': 'secret'},
        follow_redirects=True,
    )
    return client


