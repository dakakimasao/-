import joblib
import pandas as pd
from pandas import DataFrame

mlcol = ['HS', 'AS','HST', 'AST','HC', 'AC','HY', 'AY']

def predict(x:DataFrame):
    df=x
    df=df[mlcol]
    model = joblib.load('totomodel.pkl')

    prediction = model.predict(df).item()

    return prediction