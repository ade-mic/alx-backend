#!/usr/bin/env python3
"""
Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """
    Create a function to get the user based
    on the login_as parameter:
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """Use the before_request decorator
    to set the user before handling the request
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Use the _ or gettext function to parametrize your templates.
    Use the message IDs home_title and home_header.
    """
    return render_template('4-index.html',
                           home_title=_('home_title'),
                           home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
