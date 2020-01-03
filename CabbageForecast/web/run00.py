# import 
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
# instance creating
app = Flask(__name__)

# Defining the home page of our web
@ app.route("/", methods=['GET', 'POST']) # page path setting 

def index(): 
    # basic inline html
    return render_template('index.html')

if __name__ == "__main__":
    app.run( debug = True )

# It works(ok) 