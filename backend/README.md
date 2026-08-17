Backend for the "Predictive Modeling of Ground Water Depletion and Artificial Recharge Potential" project.

This FastAPI backend currently supports:
- Phase 1: health and API info endpoints
- Phase 2: groundwater prediction using the saved model
- Phase 3: artificial recharge potential assessment results from Notebook 10

How to run (development):

1. Create a virtual environment and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   pip install -r requirements.txt

2. Run the app:

   uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

API endpoints:

- GET /                     -> Project and API info
- GET /health               -> Health check with timestamp
- POST /predict             -> Groundwater level prediction using the saved trained model
- GET /recharge/summary     -> Overall recharge potential summary
- GET /recharge/stations    -> List of all station-level recharge results
- GET /recharge/stations/{station_id} -> Single station recharge assessment details

Notes:
- The recharge endpoints use the reusable CSV artifact generated from Notebook 10 logic: outputs/recharge/artificial_recharge_assessment.csv
- This assessment is a decision-support artificial recharge potential score, not measured recharge.
- Do not modify notebooks, datasets, or the trained model.
