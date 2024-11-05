#!/usr/bin/env python3
"""
setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
     Holds the configuration for
     languages (LANGUAGES), default locale
     """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get_locale function with the babel.localeselector decorator.
    Use request.accept_languages to
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('3-index.html',
                           home_title=_('home_header'),
                           home_header=_('home_title')
                            )


if __name__ == '__main__':
    app.run(debug=True)
