#!/usr/bin/python3
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



@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

app.run(host='0.0.0.0', port=5000)
