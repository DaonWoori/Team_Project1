import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

# data pre
def data_pre2(data):
    df = pd.read_csv('C:/Users/daonwoori/Downloads/team_project1/csv/binary_classification_data.csv')
    pre_df = pd.DataFrame([data], columns = [' Mean of the integrated profile', ' Standard deviation of the integrated profile', ' Excess kurtosis of the integrated profile', ' Skewness of the integrated profile', ' Mean of the DM-SNR curve', ' Standard deviation of the DM-SNR curve', ' Excess kurtosis of the DM-SNR curve', ' Skewness of the DM-SNR curve'])

    pipeline = Pipeline([('minmax', MinMaxScaler()),
                        ('Standard', StandardScaler())])
    
    X = df.drop(['target_class'], axis = 1)
    X_train, X_test = train_test_split(X, test_size= 0.2, random_state = 42)
    X_train, X_val = train_test_split(X_train, test_size = 0.2, random_state = 42)

    X_train = pipeline.fit_transform(X_train)
    pre_df = pipeline.transform(pre_df)

    return pre_df



def predict_dl2(data):
    model2 = tf.keras.models.load_model('C:/Users/daonwoori/Downloads/team_project1/models/model2.h5')
    y_pred = model2.predict(data)
    if y_pred > 0.5:
        results = 1
    else:
        results = 0

    return results