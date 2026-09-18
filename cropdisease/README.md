# Smart Crop AI MVP

24-hour hackathon MVP using React + CSS, FastAPI, SQLite, image classification API contract, and Random Forest Regression.

## Run backend
```bash
cd backend
python -m venv venv
# Windows PowerShell: .\venv\Scripts\Activate.ps1
# Windows cmd: venv\Scripts\activate.bat
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Backend: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

## Run frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173

## Notes
The yield model trains automatically from `backend/data/sample_yield_data.csv` on first startup. The disease endpoint currently uses a lightweight MVP image validation/classification fallback based on the filename; replace `backend/app/services/disease_service.py` with a trained image-classification model when the real model artifact is available, keeping the same `classify_image()` interface.
