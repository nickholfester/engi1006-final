# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""
#log
# added page title
# created static folder
# added image

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/test")
def test():
    return render_template("testing.html")

@app.route("/1006")
def homepage():
    return "1006 Home Page"

#start the server
if __name__ == "__main__":
    app.run()