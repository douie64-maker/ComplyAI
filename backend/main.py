from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel
import os

app = FastAPI(title="ComplyAI Backend")

# Trust proxy headers for HTTPS (required for cloud deployments like Render)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# CORS so all browsers can call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/ask")
def ask_ai(q: Query):
    # Placeholder AI logic (plug real LLM later)
    return {"answer": f"ComplyAI received: {q.text}"}


