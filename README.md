# 🧠 ML Model Deployment API (FastAPI + Docker)

A production-ready API for serving machine learning model predictions using **FastAPI** and **Docker**. This project demonstrates how to load a trained ML model, expose it through a REST API, and containerize the entire system for reproducible deployment.

---

## 🚀 Features

- 🧪 Trained ML model (Iris flower classifier)
- ⚙️ FastAPI-powered RESTful API
- 🐳 Dockerized for portable deployment
- 📄 Swagger UI for testing (`/docs`)
- ✅ Modular code: schema validation, routes, model loading
- 📂 Output examples included (request/response, cURL, screenshots)

---

## 📁 Project Structure
## 📂 Folder Structure

```
ml-model-deployment-api/
├── app/ # FastAPI app and logic
│ ├── main.py
│ ├── model/
│ ├── routes/
│ ├── schemas/
│ └── utils/
├── training/ # Model training pipeline
├── test/ # Tests (TBD)
├── outputs/ # Screenshots and sample inputs
├── Dockerfile # Docker container config
├── requirements.txt
├── README.md

```

---

## 📦 Tech Stack

- Python 3.10
- FastAPI
- Scikit-learn
- Docker
- Pydantic
- Uvicorn

---

## 📊 Model Info

- Dataset: Iris (from `sklearn.datasets`)
- Model: `RandomForestClassifier` embedded in a `Pipeline` with `StandardScaler`
- Output: Predicted class label + class name

---

## 📤 API Usage

### 🔗 Endpoint



POST /api/predict

### 📝 Sample Request

```json
{
  "data": [5.1, 3.5, 1.4, 0.2]
}


✅ Sample Response

{
  "prediction": 0,
  "class_name": "setosa"
}



🧪 Run Locally

1. Install dependencies

pip install -r requirements.txt

2. Train the model

python -m training.train_pipeline

3. Start API

uvicorn app.main:app --reload

4. Test in Swagger UI

Visit: http://127.0.0.1:8000/docs



🐳 Run with Docker

1. Build image

docker build -t ml-api .

2. Run container

docker run -p 8000:8000 ml-api

Visit: http://localhost:8000/docs



🧪 Output Samples

- outputs/swagger_ui.png — Screenshot of Swagger interface

- outputs/predict_response.png — Prediction result

- outputs/sample_request.json — Example input

- outputs/sample_curl.txt — cURL example
