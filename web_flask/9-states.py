#!/usr/bin/python3
""" display all cities and states in a web app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exe):
    """ removes current session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ route to show all cities by a state """
    states = storage.all(State)
    return render_template('9-states.html', states=states, url='/states')


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ displays state and its cities with specified id """
    states = storage.all(State)
    state = None
    for key, value in states.items():
        if id == value.id:
            state = value
    return render_template('9-states.html', state=state, url='/states/<id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
