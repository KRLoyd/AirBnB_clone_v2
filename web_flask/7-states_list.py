#!/usr/bin/python3
'''

'''
# Import
from flask import Flask
from flask import render_template
from models import storage

# Create an instance of Flask
app = Flask(__name__)

# Set strict_slashes for all routes
app.url_map.strict_slashes = False


# Specify teardown instx
@app.teardown_appcontext
def teardown(self):
    '''Function to remove the current SQLAlchemy Session after each request.'''
    storage.close()


# Map /states_list
@app.route('/states_list')
def states_list_route():
    '''Function to display an HTML page.'''
    # Get a dict of all States
    state_dict = storage.all(cls="State")
    # Create an empty list
    state_list = []
    # Make a list of tuples using info from state_dict
    for k, v in state_dict.items():
        state_id = k.split('.')
        state_id = state_id[1]
        state_name = v.name
        tup = (state_id, state_name)
        state_list.append(tup)
    # Sort state_list by state_name
    state_list.sort(key=lambda x: x[1])
    # return rendered template
    return render_template('7-states_list.html', list=state_list)

# Run app if __main__
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
