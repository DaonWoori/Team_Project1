from flask import Flask, render_template, request
from function.model1_ML import model1_predict, model1_data_preprocessing
from function.model2_ML import model2_predict, model2_data_preprocessing
from function.model1_dl import predict_dl, data_pre
from function.model2_dl import predict_dl2, data_pre2
from function.model3_dl import predict_dl3, data_pre3

# flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/model1', methods=['GET', 'POST'])
def model1():
    # model1에 대한 처리 로직을 구현합니다.
    if request.method == 'GET':
        return render_template('model1.html')
    
    if request.method == 'POST':
        sex = request.form['Sex']
        length = float(request.form['Length'])
        diameter = float(request.form['Diameter'])
        height = float(request.form['Height'])
        whole_weight = float(request.form['Whole_weight'])
        shucked_weight = float(request.form['Shucked_weight'])
        viscra_weight = float(request.form['Viscra_weight'])
        shell_weight = float(request.form['Shell_weight'])
        
        model = request.form['items1']
        
        if model == 'ML':
            data = model1_data_preprocessing([sex, length, diameter, height, whole_weight, shucked_weight, viscra_weight, shell_weight])
            results = model1_predict(data)
        elif model == 'DL':
            data = data_pre([sex, length, diameter, height, whole_weight, shucked_weight, viscra_weight, shell_weight, 0, 0, 0])
            results = predict_dl(data)
        return render_template('model1.html', results=results)
    
@app.route('/model2', methods=['GET', 'POST'])
def model2():
    # model2에 대한 처리 로직을 구현합니다.
    if request.method == 'GET':
        return render_template('model2.html')
    
    if request.method == 'POST':
        IP_mean = float(request.form['IP_mean'])
        IP_devi = float(request.form['IP_devi'])
        IP_kur = float(request.form['IP_kur'])
        IP_ske = float(request.form['IP_ske'])
        DM_mean = float(request.form['DM_mean'])
        DM_devi = float(request.form['DM_devi'])
        DM_kur = float(request.form['DM_kur'])
        DM_ske = float(request.form['DM_ske'])
        
        model = request.form['items1']
        
        if model == 'ML':
            data = model2_data_preprocessing([IP_mean, IP_devi, IP_kur, IP_ske, DM_mean, DM_devi, DM_kur, DM_ske])
            results = model2_predict(data)
        elif model == 'DL':
            data = data_pre2([IP_mean, IP_devi, IP_kur, IP_ske, DM_mean, DM_devi, DM_kur, DM_ske])
            results = predict_dl2(data)
        
        return render_template('model2.html', results=results)

@app.route('/model3', methods=['GET', 'POST'])
def model3():
    # model3에 대한 처리 로직을 구현합니다.
    if request.method == 'GET':
        return render_template('model3.html')
    
    if request.method == 'POST':
        cols = ['X_Minimum', 'X_Maximum', 'Y_Minimum', 'Y_Maximum', 'Pixels_Areas',
       'X_Perimeter', 'Y_Perimeter', 'Sum_of_Luminosity',
       'Minimum_of_Luminosity', 'Maximum_of_Luminosity', 'Length_of_Conveyer',
       'TypeOfSteel_A300', 'TypeOfSteel_A400', 'Steel_Plate_Thickness',
       'Edges_Index', 'Empty_Index', 'Square_Index', 'Outside_X_Index',
       'Edges_X_Index', 'Edges_Y_Index', 'Outside_Global_Index', 'LogOfAreas',
       'Log_X_Index', 'Log_Y_Index', 'Orientation_Index', 'Luminosity_Index',
       'SigmoidOfAreas']
        
        data = []
        for col in cols:
            data.append(float(request.form[col]))
        print(data)
        data = data_pre3(data)
        results = predict_dl3(data)
        print(results)

        return render_template('model3.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)