from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "sample_yield_data.csv"
MODEL_FILE = BASE_DIR / "app" / "models" / "yield_model.joblib"

FEATURES = ["crop_name", "soil_ph", "temperature", "rainfall", "humidity", "soil_moisture", "area"]
CATEGORICAL = ["crop_name"]
NUMERIC = [x for x in FEATURES if x not in CATEGORICAL]

def train_model():
    df = pd.read_csv(DATA_FILE)
    preprocessor = ColumnTransformer([
        ("crop", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
        ("num", "passthrough", NUMERIC),
    ])
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(n_estimators=150, random_state=42, min_samples_leaf=1)),
    ])
    pipeline.fit(df[FEATURES], df["yield_tons"])
    MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_FILE)
    return pipeline

def get_model():
    if not MODEL_FILE.exists():
        return train_model()
    return joblib.load(MODEL_FILE)

def predict_yield(data: dict) -> float:
    model = get_model()
    df = pd.DataFrame([data], columns=FEATURES)
    prediction = float(model.predict(df)[0])
    return max(0.0, round(prediction, 2))
