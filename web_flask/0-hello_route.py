#!/usr/bin/python3
"""
Simple flask web server
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "Hello HBNB!"

app.run(host='0.0.0.0', port=5000)
