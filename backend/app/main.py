"""
Simple FastAPI app for Phase 1 (backend setup) of the project.
Provides:
 - GET /      : basic project/API information
 - GET /health: health check

CORS is enabled for future frontend development.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pathlib import Path
import os

# Resolve project root relative to this file (works regardless of current working directory)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

app = FastAPI(
    title="Groundwater Depletion & Recharge API (Phase 1)",
    version="0.1.0",
    description="Phase 1: simple backend with health and info endpoints. Prediction endpoints will be added later.",
)

# Configure CORS for future frontend. For the academic project, allow all origins but restrict in later phases.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict origins in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"])
async def root_info():
    """Return basic project and API information."""
    # Example of using project-relative paths without hardcoding machine-specific paths
    models_dir = PROJECT_ROOT / "models"
    model_file = models_dir / "best_model.pkl"
    model_exists = model_file.exists()

    return {
        "project": "Predictive Modeling of Ground Water Depletion and Artificial Recharge Potential",
        "phase": "Phase 1 - Backend setup",
        "api_version": "0.1.0",
        "models_dir": str(models_dir),
        "model_file": str(model_file),
        "model_exists": model_exists,
        "note": "Prediction API not implemented in Phase 1. Use /health to check service status.",
    }


@app.get("/health", tags=["health"])
async def health_check():
    """Basic health endpoint returning a timestamp and simple status."""
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}


# Allow running with `python -m` as well
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
