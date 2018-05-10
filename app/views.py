# views.py

from app import app
from flask import render_template
import json
 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/data')
def get_data():
    
    obj = {
        "test_data" : [
            "hello",
            "there"
        ]
    }

    return json.dumps(obj)