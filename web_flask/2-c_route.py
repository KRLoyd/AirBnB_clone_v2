#!/usr/bin/python3
'''
Script to start a web application.

Includes the following routes:
- root (/)
- /hbnb
- /c/<text>
'''
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)


# Map root (/)
@app.route('/', strict_slashes=False)
def root_route():
    '''Function to display "Hello HBNB!" when requesting root.'''
    return 'Hello HBNB!'


# Map /hbnb
@app.route('/hbnb')
def hbnb_route():
    '''Function to display "HBNB" when requesting /hbnb.'''
    return 'HBNB'


# Map /c/<text>
@app.route('/c/<text>')
def c_route(text):
    '''Function to display "C" followed by the value of variable text.
    Spaces replace underscore symbols.
    '''
    spaced_text = text.replace('_', ' ')
    return 'C {}'.format(spaced_text)

# Run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
