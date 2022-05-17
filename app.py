#import flask dependency:
from flask import Flask

# create a New Flask App Instance:
app = Flask(__name__)

# define starting point or root route:
@app.route('/')
def hello_world():
    return 'Hello world'

# Define the about route (skill drill -9.4.3)
@app.route("/about")
def about():
    name = "Rebecca"
    location = "SC"

    return f"My name is {name}, and I live in {location}."

