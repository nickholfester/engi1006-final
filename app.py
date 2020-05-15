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

@app.route("/001")
def link1():
    return "Link 1 - In Progress"

@app.route("/002")
def link2():
    return "Link 2 - In Progress"



#start the server
if __name__ == "__main__":
    app.run()