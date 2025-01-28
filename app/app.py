from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

CORS(app)

# Load the Random Forest model
with open(r'outputs/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Load the feature names
with open(r'outputs/feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json()

        # Convert input data to a DataFrame with the expected structure
        input_data = pd.DataFrame([data["features"]], columns=feature_names[:len(data["features"])])

        # Align columns with the expected feature set, filling missing columns with 0
        input_data = input_data.reindex(columns=feature_names, fill_value=0)

        # Make prediction
        prediction = model.predict(input_data)[0]  # "Good" or "Bad"
        probability = model.predict_proba(input_data)[0].tolist()

        # Return the prediction and probability
        return jsonify({
            "prediction": prediction,  # "Good" or "Bad"
            "probability": probability
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

