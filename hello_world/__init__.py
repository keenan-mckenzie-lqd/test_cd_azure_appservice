from flask import Flask
app = Flask(__name__)

from hello_world import blueprint_1

from hello_world.blueprint_1.routes import mod

@app.route("/")
def hello():
    return "Hello World!"