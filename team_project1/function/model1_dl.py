import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer, MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf

# data pre
def data_pre(data):
    df = pd.read_csv('C:/Users/daonwoori/Downloads/team_project1/csv/Regression_data_preprocessing.csv')

    if data[0] == 'F':
        data[8] = 1
        data[9] = 0
        data[10] = 0
        data.pop(0)
    
    elif data[0] == 'I':
        data[8] = 0
        data[9] = 1
        data[10] = 0
        data.pop(0)

    elif data[0] == 'M':
        data[8] = 0
        data[9] = 0
        data[10] = 1
        data.pop(0)

    pre_df = pd.DataFrame([data], columns = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Sex_F', 'Sex_I', 'Sex_M'])

    pipeline = Pipeline([('normalizer', Normalizer()),
                        ('scaler', StandardScaler())])
    
    X = df.drop(['Rings'], axis = 1)
    X_train, X_test = train_test_split(X, test_size= 0.2, random_state = 42)
    X_train, X_val = train_test_split(X_train, test_size = 0.2, random_state = 42)

    feature_cols = pre_df.columns.tolist()
    remove_list = ['Sex_I','Sex_F','Sex_M'] 

    for col in remove_list:
        feature_cols.remove(col)

    X_train[feature_cols] = pipeline.fit_transform(X_train[feature_cols])
    pre_df[feature_cols] = pipeline.transform(pre_df[feature_cols])

 
    return pre_df



def predict_dl(data):
    model1 = tf.keras.models.load_model('C:/Users/daonwoori/Downloads/team_project1/models/model1.h5')
    prediction = model1.predict(data)
    results = 10**(prediction)
    return int(results)