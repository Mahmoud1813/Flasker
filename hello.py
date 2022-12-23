from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator 
@app.route('/')
def index():
    lst = [5, 10, 15, 20]
    #return "<h1>Hello World!</h1>"
    return render_template("index.html", lst=lst)

#localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    #return "<h1>Hello {}!</h1>".format(name)
    return render_template("user.html", name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


"""
Filters:
safe
capitalize 
lower
upper
title
trim
striptags
"""

