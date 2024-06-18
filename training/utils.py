import os
import joblib
import logging
from training.config import MODEL_DIR

def save_object(obj, filepath):
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(obj, filepath)

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s"
    )
