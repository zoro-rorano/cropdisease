from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

OUT = Path(__file__).parent / "app" / "models" / "disease_model" / "disease_model.joblib"
rng = np.random.default_rng(42)
X, y = [], []
for label in ["Healthy Leaf", "Early Blight", "Leaf Spot"]:
    for _ in range(180):
        img = np.zeros((32, 32, 3), dtype=np.float32)
        img[:, :, 1] = rng.normal(0.55, 0.08, (32, 32))
        img[:, :, 0] = rng.normal(0.18, 0.05, (32, 32))
        img[:, :, 2] = rng.normal(0.12, 0.04, (32, 32))
        if label == "Early Blight":
            for _ in range(rng.integers(2, 6)):
                cy, cx = rng.integers(4, 28, 2)
                yy, xx = np.ogrid[:32, :32]
                mask = (yy-cy)**2 + (xx-cx)**2 < rng.integers(5, 20)
                img[mask, 0] += 0.45; img[mask, 1] -= 0.20
        elif label == "Leaf Spot":
            for _ in range(rng.integers(8, 18)):
                cy, cx = rng.integers(2, 30, 2)
                yy, xx = np.ogrid[:32, :32]
                mask = (yy-cy)**2 + (xx-cx)**2 < rng.integers(2, 7)
                img[mask, :] *= 0.25
        X.append(np.clip(img, 0, 1).reshape(-1)); y.append(label)
model = RandomForestClassifier(n_estimators=120, random_state=42, n_jobs=-1)
model.fit(np.asarray(X), np.asarray(y))
OUT.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, OUT)
print(f"Saved {OUT}")
