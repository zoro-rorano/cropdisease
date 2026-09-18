from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database.database import Base, engine
from .routes import disease, history, yield_prediction
from .services.yield_service import get_model

Base.metadata.create_all(bind=engine)
get_model()  # train the small sample model on first startup

app = FastAPI(title="Smart Crop AI MVP", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5175", "http://127.0.0.1:5175"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(disease.router)
app.include_router(yield_prediction.router)
app.include_router(history.router)

@app.get("/")
def root():
    return {"message": "Smart Crop AI MVP is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
