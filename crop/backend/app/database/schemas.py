from pydantic import BaseModel, Field

class YieldInput(BaseModel):
    crop_name: str = Field(min_length=1)
    soil_ph: float = Field(ge=0, le=14)
    temperature: float = Field(ge=-50, le=70)
    rainfall: float = Field(ge=0, le=10000)
    humidity: float = Field(ge=0, le=100)
    soil_moisture: float = Field(ge=0, le=100)
    area: float = Field(gt=0, le=100000)

class YieldResponse(BaseModel):
    predicted_yield: float
    unit: str = "tons"

class DiseaseResponse(BaseModel):
    disease: str
    confidence: float
