#!/usr/bin/python3
"""
web server -> url=/python/<text>
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ root """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ c/text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ python/text """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == '__name__':
    app.run(host='0.0.0.0', port=5000)
