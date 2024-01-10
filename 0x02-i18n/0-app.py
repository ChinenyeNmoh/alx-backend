#!/usr/bin/env python3
""" 0-app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Renders a Basic Template"""
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(debug=True)
