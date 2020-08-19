from flask import Flask, request
app = Flask(__name__)

from hello_world import blueprint_1
from hello_world.models.price_model import run_price_model

from hello_world.blueprint_1.routes import mod

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/price', methods=['POST'])
def price_model():
    json_body = request.get_json(force=True)
    prediction = run_price_model(json_body)
    return {'model': 'price_model', 'prediction': prediction}