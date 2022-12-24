from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no is supposed to know"

# Create a Form class
class NamerForm(FlaskForm):
    name = StringField("What's your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


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

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()

    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form=form)



"""
Filters:
safe
capitalize 
lower
upper
title
trim
striptags

Three steps to push to git from terminal
git add .
git commit -am "message"
git push

To initiliaze version control go to:
https://codemy.com/git
"""


