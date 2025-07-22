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
│ └── schemas/
├── training/ # Model training pipeline
│ ├──__init__.py
│ ├──config.py
│ ├──train_pipeline.py
│ └──utils.py
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

## 🌐 API Usage

### 🔗 **Endpoint**

**POST** `/api/predict`

---

### 📝 **Sample Request**

```json
{
  "data": [5.1, 3.5, 1.4, 0.2]
}
```

---

### ✅ **Sample Response**

```json
{
  "prediction": 0,
  "class_name": "setosa"
}
```

---

## 🧪 Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the model

```bash
python -m training.train_pipeline
```

### 3️⃣ Start the API

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Test in Swagger UI

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Run with Docker

### 1️⃣ Build the image

```bash
docker build -t ml-api .
```

### 2️⃣ Run the container

```bash
docker run -p 8000:8000 ml-api
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🖼️ Output Samples

```
📁 outputs/
├── swagger_ui.png          – Screenshot of Swagger
├── predict_response.png    – Sample model response
├── sample_request.json     – Example request payload
├── sample_curl.txt         – Example cURL command
```
