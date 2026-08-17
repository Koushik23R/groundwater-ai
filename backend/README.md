Backend for the "Predictive Modeling of Ground Water Depletion and Artificial Recharge Potential" project.

This simple FastAPI backend (Phase 1) provides basic health and info endpoints and CORS configuration for a future frontend.

How to run (development):

1. Create a virtual environment and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt

2. Run the app:

   uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

API endpoints:

- GET /          -> Project and API basic info
- GET /health    -> Health check with timestamp

Notes:
- Do not modify notebooks or data in data/ or notebooks/ during Phase 1.
- Prediction endpoints will be implemented in later phases.
