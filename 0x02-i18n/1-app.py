#!/usr/bin/env python3
"""
setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template
from flask_babel import Babel

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


@app.route('/')
def index():
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
