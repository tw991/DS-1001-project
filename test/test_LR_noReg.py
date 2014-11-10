import pandas as pd
import csv
import numpy as np

data = pd.read_csv('bank-additional-full.csv',';')
categorical_column = ['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for column in categorical_column:
    dummy = pd.get_dummies(data[column],column)
    data = data.join(dummy)
    data = data.drop(column, 1)

data['Y'] = pd.get_dummies(data['y'])['no']
data.to_csv('bank-additional-full-dummy.csv')