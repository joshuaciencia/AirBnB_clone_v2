#!/usr/bin/python3
""" displat all states in a web app"""
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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ route to show all states """
    states = storage.all(State)
    names = {}
    for state in states.values():
        names[state.id] = state.name
    names = sorted(names.items(), key=lambda x: x[1])
    sorted_dict = collections.OrderedDict(names)
    return render_template('7-states_list.html', states=sorted_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
