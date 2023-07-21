from flask import Flask, request, jsonify
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return "hello"

@app.route('/predict',methods=['POST'])
def predict():
    text=request.form.get('text')
    input_query=np.array([text])
    result=(summary())
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)