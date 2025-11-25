import pandas as pd
from catboost import CatBoostClassifier, Pool
from pandas import DataFrame
from sklearn.model_selection import train_test_split
import joblib

features = ['HS','AS','HST','AST','HC','AC','HY', 'AY']

def makeml (x:DataFrame):
    df=pd.DataFrame(x)

    X=df[features]
    y=df['FTR']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

    model = CatBoostClassifier(iterations=500,depth=6,learning_rate=0.05,loss_function='MultiClass',verbose=100)

    model.fit(X_train, y_train)
    
    pred= model.predict(X_test)
    score=model.score(X_test, y_test)

    model.save_model('totomodel.cbm')
    joblib.dump(model, 'totomodel.pkl')



