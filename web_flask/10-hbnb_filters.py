#!/usr/bin/python3
""" display all cities and states in a web app hbnb filters"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exe):
    """ removes current session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    sts = storage.all(State)
    ame = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', sts=sts, ame=ame)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
