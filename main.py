from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(
    title="AI Content Analyzer API",
    description="Text preprocessing and rule-based sentiment analysis API.",
    version="1.0.0"
)

class TextPayload(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    cleaned_text: str
    word_count: int
    sentiment: str
    score: float

def preprocess(text: str) -> str:
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split()).lower()

def analyze(text: str):
    positive_words = {"good", "great", "awesome", "excellent", "revolutionizing", "love", "best", "like"}
    negative_words = {"bad", "worst", "terrible", "horrible", "hate", "poor", "slow"}
    
    words = text.split()
    if not words:
        return "neutral", 0.0
        
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    
    score = (pos_count - neg_count) / len(words)
    
    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
        
    return sentiment, round(score, 2)

@app.post("/analyze", response_model=AnalysisResult)
def analyze_content(payload: TextPayload):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
        
    cleaned = preprocess(payload.text)
    sentiment, score = analyze(cleaned)
    
    return AnalysisResult(
        cleaned_text=cleaned,
        word_count=len(cleaned.split()),
        sentiment=sentiment,
        score=score
    )

@app.get("/")
def root():
    return {"message": "AI Content Analyzer API is running smoothly!"}
