#!/usr/bin/env python3
"""app config"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get_locale
    """
    return return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config(object):
    """Configure the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home():
    """Renders a Basic Template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
