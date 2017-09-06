#!/usr/bin/python3
'''
Script to start a web application.

Includes the following routes:
- root (/)
- /hbnb
- /c/<text>
- /python/<text>
- /number/<n>
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
@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''Function to display "HBNB" when requesting /hbnb.'''
    return 'HBNB'


# Map /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''Function to display "C" followed by the value of variable text.
    Spaces replace underscore symbols.
    '''
    spaced_text = text.replace('_', ' ')
    return 'C {}'.format(spaced_text)


# Map /python/<text>
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    '''Function to display "Python" followed by the value of variable text.
    Underscores in text are replaced with spaces.
    The default value of text is "is cool".
    '''
    spaced_text = text.replace('_', ' ')
    return 'Python {}'.format(spaced_text)


# Map /number/<n>
@app.route('/number/<int:n>')
def number_route(n):
    '''Function that displays "<passed number> is a number" when requesting
/number/<n>.
    n must be an integer.
    '''
    return '{} is a number'.format(n)

# Run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
