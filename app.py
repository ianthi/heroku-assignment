# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:35:25 2020

@author: User
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'
@app.route('/template')
def template():
    return render_template('question6.html')

if __name__ == '__main__':
    app.run(debug=True)