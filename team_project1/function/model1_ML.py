import numpy as np
import pandas as pd
import pickle
import math

def model1_predict(data):
    with open('C:/Users/daonwoori/Downloads/team_project1/models/regression_ML.pickle','rb') as f:
        model = pickle.load(f)
        results = int(np.round(np.exp(model.predict(data))))
    return results

def model1_data_preprocessing(data):
    # 인코딩
    if data[0] == 'M':
        data[0] = 2
    elif data[0] == 'F':
        data[0] = 0
    elif data[0] == 'I':
        data[0] = 1  
        
    cols = ['Sex_Encoded', 'Length', 'Diameter', 'Height', 'Whole weight',
       'Shucked weight', 'Viscera weight', 'Shell weight']
    df = pd.DataFrame([data], columns=cols) 
        
    # 특성공학
    df['Volume'] = 4/3 * math.pi * df['Length'] * df['Diameter'] * df['Height'] * 1/2 * 1/2
    df['Density'] = df['Shell weight'] / df['Volume']
    
    return df
