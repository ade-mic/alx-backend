#!/usr/bin/env python3
"""
Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

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


@babel.localeselector
def get_locale():
    """
    get_locale function with the babel.localeselector decorator.
    Use request.accept_languages to
    determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locals in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
