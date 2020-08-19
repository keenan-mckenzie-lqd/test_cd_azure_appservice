#!/usr/bin/env python
# coding: utf-8

# Import libraries
import pandas as pd
from sklearn import linear_model
from joblib import dump, load


#loading data - change to json later


##TODO: Read json into df

def run_price_model(json):
    df = pd.json_normalize(json)
    # input
    x = df[['Units', 'SQ']]
    # output
    y = df['Price']

    # load model
    clf = load(r'hello_world\models\PriceModel.joblib') 

    # Make predictions
    y_pred = clf.predict(x)

    return str(y_pred)


