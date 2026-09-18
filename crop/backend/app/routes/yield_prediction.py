from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..database.models import Prediction
from ..database.schemas import YieldInput, YieldResponse
from ..services.yield_service import predict_yield

router = APIRouter(prefix="/api/predict", tags=["yield"])

@router.post("/yield", response_model=YieldResponse)
def yield_prediction(payload: YieldInput, db: Session = Depends(get_db)):
    value = predict_yield(payload.model_dump())
    db.add(Prediction(prediction_type="yield", crop_name=payload.crop_name, predicted_yield=value))
    db.commit()
    return YieldResponse(predicted_yield=value)
