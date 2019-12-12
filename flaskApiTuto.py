# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:16:48 2019

@author: Raphaël Chalicarne
@github : https://github.com/raphaelchalicarne
Tutoriel from https://www.fernandomc.com/posts/your-first-flask-api/
"""

# We import Flask
from flask import Flask
    
# We create a Flask app
app = Flask(__name__)

# We establish a Flask route so that we can serve HTTP traffic on that route 
@app.route('/')
def weather():
    # We hardcode some information to be returned
    return "{'Temperature': '50'}"

# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    app.run(debug=True)