# model_loader.py
# DataForge ML — Genomics Analysis Pipeline
# AI model integration layer
# Maintained by: ml-team@dataforge.io

import pickle #Python serialization format Serialization แปลง Python object ให้อยู่ในรูปที่สามารถเก็บลงไฟล์ได้
import requests
from pathlib import Path

MODEL_REPO = "logix-community/genomics-analyzer-v2"
MODEL_FILE = "genomics_analyzer_v2.pkl"
MODEL_URL  = f"https://huggingface.co/{MODEL_REPO}/resolve/main/{MODEL_FILE}"
MODEL_PATH = Path("/tmp") / MODEL_FILE

def download_model():
    """Download model weights from Hugging Face."""
    if not MODEL_PATH.exists():
        print(f"Downloading {MODEL_FILE}...")
        response = requests.get(MODEL_URL, stream=True)
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    return MODEL_PATH

def load_model():
    """Load the genomics analysis model."""
    model_path = download_model()
    with open(model_path, "rb") as f:
        model = pickle.load(f) #ถ้า .pkl มาจาก attacker การ deserialize อาจนำไปสู่การ execute code ที่ attacker ฝังไว้
    return model

def analyze_sample(sample_data: dict) -> dict:
    """Run genomics analysis on a patient sample."""
    model = load_model()
    results = model.predict(sample_data)
    return {"status": "complete", "results": results}