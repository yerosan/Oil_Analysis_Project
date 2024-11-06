from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React

# Define your routes
@app.route('/api/predict', methods=['GET'])
def predict():
    # Replace this with your model prediction logic
    return jsonify({'message': 'Prediction data here'})

@app.route('/api/metrics', methods=['GET'])
def metrics():
    # Return metrics like RMSE, MAE, etc.
    return jsonify({
        'MAE': 2.007,
        'MSE': 8.475,
        'RMSE': 2.911,
        'R2 Score': 0.979,
        'MAPE': 0.035
    })

@app.route('/get_model_data', methods=['GET'])
def get_model_data():
    # Load y_test and test_predict data
    y_test = np.load("y_test.npy").tolist()
    test_predict = np.load("test_predict.npy").tolist()
    # Return as JSON
    return jsonify({"y_test": y_test, "test_predict": test_predict})

if __name__ == '__main__':
    app.run(debug=True)
