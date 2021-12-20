from flask import Flask
import numpy as np
from joblib import load
app = Flask(__name__)



@app.route("/")
def hello_world():
    input_data = np.array([[2],[3],[22],[10]])
    model = load('model.joblib')
    predicts = model.predict(input_data)
    return str(predicts)
    

