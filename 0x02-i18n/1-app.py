#!/usr/bin/env python3
"""
setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
