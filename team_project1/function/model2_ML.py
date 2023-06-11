import numpy as np
import pandas as pd
import pickle
import math

def model2_predict(data):
    with open('C:/Users/daonwoori/Downloads/team_project1/models/bi_classification_ML.pickle','rb') as f:
        model = pickle.load(f)
    return model.predict(data)

def model2_data_preprocessing(data):
    cols =[' Mean of the integrated profile',
       ' Standard deviation of the integrated profile',
       ' Excess kurtosis of the integrated profile',
       ' Skewness of the integrated profile', 
       ' Mean of the DM-SNR curve',
       ' Standard deviation of the DM-SNR curve',
       ' Excess kurtosis of the DM-SNR curve',
       ' Skewness of the DM-SNR curve']
    
    df = pd.DataFrame([data], columns=cols) 
    
    return df
