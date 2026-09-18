from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..database.models import Prediction
from ..database.schemas import DiseaseResponse
from ..services.disease_service import classify_image

router = APIRouter(prefix="/api/predict", tags=["disease"])

@router.post("/disease", response_model=DiseaseResponse)
async def disease_prediction(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    contents = await file.read()
    try:
        disease, confidence = classify_image(contents, file.filename or "")
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid image file") from exc
    db.add(Prediction(prediction_type="disease", disease=disease, confidence=confidence))
    db.commit()
    return DiseaseResponse(disease=disease, confidence=confidence)
