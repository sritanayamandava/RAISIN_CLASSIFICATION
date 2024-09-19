from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('D:/SMART, PROJECT-1/flask/model/raisin_classification_model.pkl')
scaler = joblib.load('D:/SMART, PROJECT-1/flask/model/raisin_scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def index1():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [float(x) for x in request.form.values()]
        features_scaled = scaler.transform([features])
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        prediction_label = 'Besni' if prediction == 0 else 'Kecimen'
        
        return jsonify({'prediction': prediction_label})
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
