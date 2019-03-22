# My { Adjective } Story

**Authors**: Chris Ball, Paul Williamsen, Evy Haan

**version**: 1.0.0

## Overview
Everyone loves a good MadLib. We wanted to build on the game by creating a more dynamic version. As usual, users can choose from a list of stories, but our site features unique functionality to randomizate the words that can be useds for prompts. The user can ever predict what words they'll be asked or where in the story they will be used, making the story even more dynamic. No story will ever be the same.

## Getting Started
1. Setup a virtual shell environment, including installation of the packages and dependencies as referenced in the Architecture section.

2. In a .env file, include:
```
FLASK_APP=src/wsgi.py
FLASK_ENV=development
DATABASE_URL= # include url to local database
SECRET_KEY= # Generate a uuid with `python3 -c "import uuid; print(uuid.uuidv4())"`
```
3. Add any .editorconfig, .gitignore, and any additional config files.

4. Create a database in Postgres. In from the terminal in the virtual environment launch SQLAlchemy, using commands: `flask db init`, `flask db migrate`, and `flask db upgrade`. This will instantiate the tables.

5. Begin a flask session using `flask run` in the terminal, and navigate to localhost:5000/test_stories. This will populate the pre-fabricated stories into the PresetStories table.

You are now ready to go!

## Architecture
#### Languages + Frameworks:

Python, Flask, HTML5, CSS3, jQuery

#### Packages:
- _flask_
- _flask-migrate_
- _flask-sqlalchemy_
- _flask-wtf_
- _gunicorn_
- _passlib_
- _psychopg2-binary_
- _python-dotenv_
- _requests_
- _uuid_

#### Dev Packages:
- _autopep8_
- _pep8_
- _pytest_
- _pytest-cov_

## Attribution
The stories we used in our application were borrowed from https://www.momjunction.com/articles/moral-stories-for-kids_00369197/.

The jQuery we used for our changing title was adapted from http://leo.dolcepixels.com/learning/jquery/snippets/random-text-from-array-with-jquery-v-2/.
