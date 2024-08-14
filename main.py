from flask import Flask, render_template, request, jsonify

import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

# Load your model
with open('models/clf2.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('models/train_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Get form data
        features = [
            int(request.form['limit_bal']),
            int(request.form['sex']),
            int(request.form['education']),
            int(request.form['marriage']),
            int(request.form['age'])
        ]

        # Add PAY_1 to PAY_6
        for i in range(1,7):
            features.append(int(request.form[f'pay_{i}']))

        # Add BILL_AMT1 to BILL_AMT6
        for i in range(1, 7):
            features.append(int(request.form[f'bill_amt{i}']))

        # Add PAY_AMT1 to PAY_AMT6
        for i in range(1, 7):
            features.append(int(request.form[f'pay_amt{i}']))

        # Make prediction
        prediction = model.predict([features])
        prediction_result = "Default likely" if prediction[0] == 1 else "Default unlikely"
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(prediction_result=prediction_result)

        return render_template('home.html',prediction_result=prediction_result)
    else:
        return render_template('home.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
