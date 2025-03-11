from flask import Flask, request, jsonify
import joblib
from fraud_detection.predict import predict_fraud
from fraud_detection.model import train_fraud_model

app = Flask(__name__)

# CORS để cho phép kết nối từ Odoo, SAP, ERP
from flask_cors import CORS
CORS(app)

# Load model
MODEL_PATH = "fraud_model.pkl"

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Fraud Detection API"})


@app.route("/predict", methods=["POST"])
def predict():
    """
    API nhận dữ liệu giao dịch và trả về dự đoán gian lận
    """
    try:
        data = request.get_json()  # Nhận dữ liệu từ request
        prediction = predict_fraud(data, MODEL_PATH)
        return jsonify({"result": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/train", methods=["GET"])
def train():
    """
    API để huấn luyện lại mô hình khi có dữ liệu mới
    """
    try:
        train_fraud_model(MODEL_PATH)
        return jsonify({"message": "Mô hình đã được huấn luyện lại thành công!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/model-info", methods=["GET"])
def model_info():
    """
    API để lấy thông tin mô hình
    """
    try:
        model = joblib.load(MODEL_PATH)
        return jsonify({"message": "Mô hình AI phát hiện gian lận", "n_estimators": len(model.estimators_)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
