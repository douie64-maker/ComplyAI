import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ComplyAI Backend")

# Get frontend URL from environment, default to localhost
frontend_url = os.getenv("NEXT_PUBLIC_BACKEND_URL", "http://localhost:3000")
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    frontend_url,
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

@app.get("/health")
def health_check():
    """Health check endpoint for cloud deployments"""
    return {"status": "ok", "service": "complyai-backend"}

@app.get("/clients")
def get_clients():
    return clients

@app.post("/clients")
def add_clients(new_clients: list):
    clients.extend(new_clients)
    return {"status": "clients added", "count": len(clients)}

@app.post("/clients/reset")
def reset_clients():
    clients.clear()
    return {"status": "clients reset"}

@app.get("/")
def root():
    return {"service": "ComplyAI Backend", "docs": "/docs"}
