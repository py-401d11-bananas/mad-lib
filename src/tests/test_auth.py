import pytest


@pytest.mark.skip()
def test_get_register_status(client):
    res = client.get('/register')
    assert res.status_code == 200


@pytest.mark.skip()
def test_get_register_has_correct_title(client):
    res = client.get('/register')
    assert b'<title>Register</title>' in res.data


@pytest.mark.skip()
def test_has_correct_nav_when_not_logged_in(client):
    res = client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/login"' in res.data
    assert b'<a href="/saved"' not in res.data
    assert b'<a href="/logout"' not in res.data


@pytest.mark.skip()
def test_has_correct_nav_when_logged_in(authenticated_client):
    res = authenticated_client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/login"' not in res.data
    assert b'<a href="/saved"' in res.data
    assert b'<a href="/logout"' in res.data


@pytest.mark.skip()
def test_register_new_user(client):
    cred = {'username': 'potroast', 'password': 'delicious'}
    res = client.post('/register', data=cred, follow_redirects=True)
    assert b'<title>Register</title>' in res.data
    assert b'potroast has already been registered!' not in res.data


@pytest.mark.skip()
def test_register_new_user(client):
    cred = {'username': 'potroast', 'password': 'delicious'}
    res = client.post('/register', data=cred, follow_redirects=True)
    res = client.post('/register', data=cred, follow_redirects=True)
    assert b'<title>Register</title>' in res.data
    assert b'potroast has already been registered!' in res.data


@pytest.mark.skip()
def test_get_login_status(client):
    res = client.get('/login')
    assert res.status_code == 200


@pytest.mark.skip()
def test_get_login_title(client):
    res = client.get('/login')
    assert b'<title>Login</title>' in res.data


@pytest.mark.skip()
def test_successful_login_status(authenticated_client):
    res = authenticated_client.get('login')
    assert res.status_code == 200


@pytest.mark.skip()
def test_logout_status():
    res = authenticated_client.get('/logout', follow_redirects=True)
    assert res.status_code == 200


@pytest.mark.skip()
def test_logout_title():
    res = authenticated_client.get('/logout', follow_redirects=True)
    assert b'<title>Login</title>' in res.data


@pytest.mark.skip()
def test_protected_route(client):
    res = client.get('/saved')
    assert res.status_code == 404


@pytest.mark.skip()
def test_nonexistent_route(client):
    res = client.get('/potato')
    assert res.status_code == 404
