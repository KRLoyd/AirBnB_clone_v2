#!/usr/bin/python3
'''
Script to start a Flask web application.
'''
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)


# Map root /
@app.route('/')
def root_route(strict_slashed=False):
    '''Function to display "Hello HBNB!" when requesting root.'''
    return 'Hello HBNB!'


# Map /hbnb
@app.route('/hbnb')
def hbnb_route():
    '''Function to display "HBNB" when requesting /hbnb.'''
    return 'HBNB'

# Run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
