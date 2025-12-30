import os
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Capturar dados do formulário
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        features = np.array([[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        features_scaled = np.array([[
            age,
            trestbps, 
            chol, 
            thalach, 
            oldpeak, 
            ca
        ]])

        scaled_values = scaler.transform(features_scaled)

        features_final = np.array([[
        scaled_values[0][0],  # age
        sex,
        cp,
        scaled_values[0][1],  # trestbps
        scaled_values[0][2],  # chol
        fbs,
        restecg,
        scaled_values[0][3],  # thalach
        exang,
        scaled_values[0][4],  # oldpeak
        slope,
        scaled_values[0][5],  # ca
        thal
        ]])

        prediction = model.predict(features_final)[0]
        probability = model.predict_proba(features_final)[0][1]
        if prediction == 1:
            resultado = "Alto risco de doença cardíaca"
            img = 'resposta_negativa.png'
        else:
            resultado = "Baixo risco de doença cardíaca"
            img = 'resposta_positivo.png'

        return render_template(
            'index.html',
            img=img,
            prediction_text=resultado,
            probability=f"{probability * 100:.2f}%"
        )

    except Exception as e:
        return f"Erro na predição: {e}"
    
@app.route('/informacoes')
def informacoes():
    return render_template('informacoes.html')


if __name__ == '__main__':
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug)
