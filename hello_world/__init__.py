from flask import Flask, request
app = Flask(__name__)

from hello_world.models.price_model.price_model import run_price_model
from hello_world.models.rise_classification.inflow_clasification import df_run_CashInflow

@app.route("/")
def hello():
    return "Hello Lester!"

@app.route('/price', methods=['POST'])
def price_model():
    json_body = request.get_json(force=True)
    prediction = run_price_model(json_body)
    return {'model': 'price_model', 'prediction': prediction}

@app.route('/classify', methods=['POST'])
def classification_model():
    json_body = request.get_json(force=True)
    result = df_run_CashInflow(json_body) 
    return {'model': 'price_model', 'prediction': result}