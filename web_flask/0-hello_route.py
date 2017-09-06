#!/usr/bin/python3
'''
Script to start a Flask web application.
'''
# Import necessary packages
from flask import Flask

# create an instance of Flask
app = Flask(__name__)


# map root to function
@app.route('/', strict_slashes=False)
def hello_route():
    '''Function to return "Hello HBNB!" when requesting root '''
    return 'Hello HBNB!'

# run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
