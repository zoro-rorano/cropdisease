from io import BytesIO
from pathlib import Path
import joblib
import numpy as np
from PIL import Image

MODEL_FILE = Path(__file__).resolve().parents[1] / "models" / "disease_model" / "disease_model.joblib"


def _features(contents: bytes) -> np.ndarray:
    image = Image.open(BytesIO(contents)).convert("RGB").resize((32, 32))
    arr = np.asarray(image, dtype=np.float32) / 255.0
    return arr.reshape(1, -1)


def classify_image(contents: bytes, filename: str = "") -> tuple[str, float]:
    if not MODEL_FILE.exists():
        raise RuntimeError("Disease model is missing")
    model = joblib.load(MODEL_FILE)
    x = _features(contents)
    probabilities = model.predict_proba(x)[0]
    index = int(np.argmax(probabilities))
    return str(model.classes_[index]), float(probabilities[index])
