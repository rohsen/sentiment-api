# Sentiment Analysis REST API (FastAPI)

A small NLP service that classifies text sentiment (positive/neutral/negative) and returns polarity metrics.

## Tech
- Python, FastAPI
- TextBlob (sentiment scoring)
- Auto-generated OpenAPI docs via FastAPI

## Endpoints
- GET `/health` – service health check
- POST `/predict` – sentiment prediction for input text

## Run locally (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
