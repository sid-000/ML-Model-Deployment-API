import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
