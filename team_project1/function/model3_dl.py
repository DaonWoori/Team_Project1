import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf

# data pre
def data_pre3(data):
    cols = ['X_Minimum', 'X_Maximum', 'Y_Minimum', 'Y_Maximum', 'Pixels_Areas',
       'X_Perimeter', 'Y_Perimeter', 'Sum_of_Luminosity',
       'Minimum_of_Luminosity', 'Maximum_of_Luminosity', 'Length_of_Conveyer',
       'TypeOfSteel_A300', 'TypeOfSteel_A400', 'Steel_Plate_Thickness',
       'Edges_Index', 'Empty_Index', 'Square_Index', 'Outside_X_Index',
       'Edges_X_Index', 'Edges_Y_Index', 'Outside_Global_Index', 'LogOfAreas',
       'Log_X_Index', 'Log_Y_Index', 'Orientation_Index', 'Luminosity_Index',
       'SigmoidOfAreas']
    pre_df = pd.DataFrame([data], columns = cols)
    pre_df = pre_df.drop(['Outside_Global_Index','SigmoidOfAreas'], axis = 1)    
    X_train = pd.read_csv('C:/Users/daonwoori/Downloads/team_project1/csv/X_fi_train.csv')
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    pre_df = scaler.transform(pre_df)

    return pre_df

def predict_dl3(data):
    model3 = tf.keras.models.load_model('C:/Users/daonwoori/Downloads/team_project1/models/model3.h5')
    y_pred = model3.predict(data)
    
    # 조건을 만족하는 원소의 인덱스 찾기
    indices = np.where(y_pred > 0.5)

    # 첫 번째 차원의 인덱스 가져오기
    indices = indices[1]
    results = int(indices[0])

    if results == 0:
        ans = 'Pastry'
    elif results == 1:
        ans = 'Z_Scratch'
    elif results == 2:
        ans = 'K_Scratch'
    elif results == 3:
        ans = 'Stains'
    elif results == 4:
        ans = 'Dirtiness'
    elif results == 5:
        ans = 'Bumps'
    elif results == 6:
        ans = 'Other_Faults'

    return ans