# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:30:52 2019

@author: Raphaël Chalicarne
@github : https://github.com/raphaelchalicarne
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'