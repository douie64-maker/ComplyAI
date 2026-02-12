import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ComplyAI Backend")

# Allow requests from any origin so the app works from any browser/cloud URL.
# In production you can restrict this to specific origins via the ALLOW_ORIGINS env var.
allow_origins_env = os.getenv("ALLOW_ORIGINS", "*")
if allow_origins_env.strip() == "*":
    cors_origins = ["*"]
else:
    cors_origins = [o.strip() for o in allow_origins_env.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
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
