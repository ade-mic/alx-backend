#!/usr/bin/env python3
"""
Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header.
"""
from flask import Flask, render_template
from flask_babel import Babel, _
from datetime import datetime
import pytz

app = Flask(__name__)
class Config:
    """
    Configuration class with supported
    languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Use the _ or gettext function to parametrize your templates.
    Use the message IDs home_title and home_header.
    """
    return render_template('3-index.html',
                           home_title=_('home_title'),
                           home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
