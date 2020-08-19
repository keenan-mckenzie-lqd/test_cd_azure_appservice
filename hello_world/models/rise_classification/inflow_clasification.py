#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import string
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from joblib import dump, load

def df_run_CashInflow(json):
    
    #loading data of csv
    df = pd.json_normalize(json)

    # input, name of column values looked at 
    x = df['Source Description']

    # load model
    clf = load(r'hello_world/models/rise_classification/InflowClassification_model.joblib') 

    # Make predictions, has to be looped through the array for more than 1 output
    
    y_pred = clf.predict(x)
    
    return str(y_pred)


# In[ ]:




