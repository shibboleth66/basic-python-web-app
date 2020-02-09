# views.py

# import json
from app import application
from flask import render_template, request

@application.route('/')
@application.route('/index.html')
def index():
    return render_template("index.html")

@application.route('/about')
def about():
    return render_template("about.html")

@application.route('/details')
def details():
    import os
    return render_template("details.html", list=os.environ)
