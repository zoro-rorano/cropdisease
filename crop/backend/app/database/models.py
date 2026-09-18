from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String
from .database import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    prediction_type = Column(String, nullable=False)
    crop_name = Column(String, nullable=True)
    disease = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    predicted_yield = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
