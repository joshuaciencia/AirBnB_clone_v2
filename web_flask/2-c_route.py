#!/usr/bin/python3
"""
web server flask url=/c/<text>
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace('_', ' '))

app.run(host='0.0.0.0', port=5000)
