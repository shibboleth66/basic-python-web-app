# views.py

from app import application
from flask import render_template
import json
 
@application.route('/')
@application.route('/index.html')
def index():
    return render_template("index.html")

@application.route('/about')
def about():
    return render_template("about.html")

@application.route('/data')
def get_data():
    
    obj = {
        "test_data" : [
            "hello",
            "there"
        ]
    }

    return json.dumps(obj)
