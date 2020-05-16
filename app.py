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
import pandas as pd

#Flask app variable
app = Flask(__name__)


# making class data-frame for /classes
df = pd.DataFrame({'Class': ['Accelerated Physics II', 'Intro to PDE', 'Fourier Analysis', \
                             'Intro to Comp.', 'Physics of Atmo/Ocean'],
                   'Department': ['Physics', 'Applied Math', 'Math', 'Engineering', 'Environ.'],
                   'Course ID': ['PHYS UN2802', 'APMA E3102', 'MATH GU4032', 'ENGI E1006', 'EESC GU4930'],
                   'Professor': ['Cole', 'Tippett', 'Woit', 'Paine', 'Gordon']})

#static route
@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/weather")
def link1():
    return render_template("weather.html")

@app.route("/classes")
def classes():
    return render_template("classes.html", tables=[df.to_html(classes='data', header="true", index=False)])



#start the server
if __name__ == "__main__":
    app.run()