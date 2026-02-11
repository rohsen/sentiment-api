from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from textblob import TextBlob
import time

app = FastAPI(title="Sentiment API", version="1.0.0")

class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)

class PredictResponse(BaseModel):
    sentiment: str
    polarity: float
    subjectivity: float
    latency_ms: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    start = time.time()

    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text must not be empty.")

    blob = TextBlob(text)
    polarity = float(blob.sentiment.polarity)          # -1..1
    subjectivity = float(blob.sentiment.subjectivity)  # 0..1

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    latency_ms = int((time.time() - start) * 1000)

    return PredictResponse(
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        latency_ms=latency_ms,
    )
