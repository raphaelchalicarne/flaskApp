# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:30:52 2019

@author: Raphaël Chalicarne
@github : https://github.com/raphaelchalicarne
"""

from flask import Flask
from flask import escape
app = Flask(__name__)

# %% Routing

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# %% Variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)