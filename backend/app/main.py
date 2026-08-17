"""FastAPI backend for the groundwater depletion prediction project.

Phase 1 provided the backend shell and health endpoints. This file now hosts
Phase 2 prediction functionality while keeping the original route behavior intact.
"""
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from backend.app.model_service import get_model_name, get_model_features, predict_groundwater_level
from backend.app.schemas import PredictionRequest

PROJECT_ROOT = Path(__file__).resolve().parents[2]

app = FastAPI(
    title="Groundwater Depletion & Recharge API",
    version="0.2.0",
    description="Academic project backend for groundwater depletion prediction and later recharge analysis.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"])
async def root_info():
    """Return basic project and API information."""
    models_dir = PROJECT_ROOT / "models"
    model_file = models_dir / "best_model.pkl"
    model_exists = model_file.exists()

    return {
        "project": "Predictive Modeling of Ground Water Depletion and Artificial Recharge Potential",
        "phase": "Phase 2 - Prediction API",
        "api_version": "0.2.0",
        "models_dir": str(models_dir),
        "model_file": str(model_file),
        "model_exists": model_exists,
        "model_name": get_model_name(),
        "feature_count": len(get_model_features()),
        "note": "Prediction endpoint is available via POST /predict. Recharge and explainability endpoints will be added later.",
    }


@app.get("/health", tags=["health"])
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}


@app.post("/predict", tags=["prediction"])
async def predict(request: PredictionRequest):
    """Predict groundwater level using the saved trained model and metadata-driven feature order."""
    try:
        prediction_value = predict_groundwater_level(request.dict())
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": str(exc), "error_type": "missing_model_file"},
        ) from exc
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"status": "error", "message": str(exc), "error_type": "missing_features"},
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"status": "error", "message": str(exc), "error_type": "invalid_input"},
        ) from exc
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": str(exc), "error_type": "model_prediction_failed"},
        ) from exc
    except Exception as exc:  # pragma: no cover - broad safety net for unexpected issues.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"status": "error", "message": "Unexpected model prediction error.", "error_type": "unexpected_error"},
        ) from exc

    return {
        "status": "success",
        "predicted_groundwater_level": prediction_value,
        "model_name": get_model_name(),
        "feature_count": len(get_model_features()),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
