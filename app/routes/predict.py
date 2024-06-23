from fastapi import APIRouter, HTTPException
from app.schemas.input_output import IrisInput, PredictionResponse
from app.model.load_model import load_model
from sklearn.datasets import load_iris

router = APIRouter()
model = load_model()
target_names = load_iris().target_names

@router.post("/predict", response_model=PredictionResponse)
def predict(input_data: IrisInput):
    if len(input_data.data) != 4:
        raise HTTPException(status_code=400, detail="Expected 4 features for Iris data.")
    
    prediction = model.predict([input_data.data])[0]
    class_name = target_names[prediction]
    return PredictionResponse(prediction=prediction, class_name=class_name)
