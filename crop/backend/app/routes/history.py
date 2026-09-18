from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..database.models import Prediction

router = APIRouter(prefix="/api/predictions", tags=["history"])

@router.get("")
def history(db: Session = Depends(get_db)):
    rows = db.query(Prediction).order_by(Prediction.created_at.desc()).limit(50).all()
    return [{
        "id": r.id, "prediction_type": r.prediction_type, "crop_name": r.crop_name,
        "disease": r.disease, "confidence": r.confidence,
        "predicted_yield": r.predicted_yield,
        "created_at": r.created_at.isoformat(),
    } for r in rows]
