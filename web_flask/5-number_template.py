#!/usr/bin/python3
'''
Script to start a web application.

Includes the following routes:
- root (/)
- /hbnb
- /c/<text>
- /python/<text>
- /number/<n>
- /number_template/<n>
'''
# Import Flask and render_template
from flask import Flask
from flask import render_template

# Create an instance of Flask
app = Flask(__name__)

# Set strict_slashes for all routes
app.url_map.strict_slashes = False


# Map root (/)
@app.route('/')
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


# Map /python/<text>
@app.route('/python/')
@app.route('/python/<text>')
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


# Map /number_template/<n>
@app.route('/number_template/<int:n>')
def number_template_route(n):
    '''Function to display an HTML page if n is an integer.'''
    return(render_template('5-number.html', n=n))

# Run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
