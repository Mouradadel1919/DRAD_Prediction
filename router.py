import numpy as np 
import pandas as pd 
import pickle

from flask import Flask, render_template, request
from Utils import preprocess_new


with open('LinearRegression.pkl', 'rb') as file:
    model = pickle.load(file)
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/predict", methods= ["GET", "POST"])
def predict():
    if request.method == "POST":
        depth = request.form['Measured Depth']
        GR    = request.form['GR']
        NPHI  = request.form['NPHI']
        RHOB  = request.form['RHOB']
        RT    = request.form['RT']
        URAN  = request.form['URAN']
        THOR  = request.form['THOR']
        K = request.form['K']
        ki = request.form['ki']
        eUi = request.form['eUi']
        KD = request.form['KD%']
        eUD = request.form['eUD%']

        X_new = pd.DataFrame({'Measured Depth': [depth], 'GR': [GR], 'NPHI': [NPHI], 'RHOB': [RHOB],
                              'RT': [RT],'THOR': [THOR], 'URAmouradadel313/drad_flaskN': [URAN],  'K': [K],
                              'ki': [ki], 'eUi': [eUi], 'KD%': [KD],
                              'eUD%': [eUD]
                              })

        # Call the Function and Preprocess the New Instances
        X_processed = preprocess_new(X_new)
        y_pred_final = model.predict(X_processed)

        return render_template('predict.html', y_pred= y_pred_final)
    else:
        return render_template('predict.html')

    

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



