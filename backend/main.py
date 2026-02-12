from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS so all browsers can call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # lock this down later
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

