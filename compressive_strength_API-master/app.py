from flask import Flask, request, jsonify
import pickle
import numpy as np
import sklearn

model_from = pickle.load(open('model.pkl','rb'))
model_to = pickle.load(open('model1.pkl','rb'))

app =Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/predict', methods =['POST'])
def predict():
    grade = int(request.form.get('GRADE'))
    upv = float(request.form.get('UPV'))
    rebound = float(request.form.get('REBOUND'))
    age = float(request.form.get('AGE'))


    input_query_from =  np.array([[grade,upv,rebound,age]])
    input_query_to = np.array([[grade, upv, rebound, age]])

    result_from = model_from.predict(input_query_from)[0]
    result_to = model_to.predict(input_query_to)[0]

    return jsonify({'FROM':str(result_from)},{'TO': str(result_to)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)