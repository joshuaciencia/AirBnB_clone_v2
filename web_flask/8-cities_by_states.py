#!/usr/bin/python3
""" display all cities and states in a web app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import collections
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exe):
    """ removes current session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ route to show all cities by a state """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
