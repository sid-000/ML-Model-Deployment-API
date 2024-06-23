from pydantic import BaseModel
from typing import List

class IrisInput(BaseModel):
    data: List[float]

class PredictionResponse(BaseModel):
    prediction: int
    class_name: str
