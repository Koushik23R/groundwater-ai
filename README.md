# Groundwater AI

This repository contains the machine learning workflow for groundwater level prediction in Bengaluru. The project focuses on data cleaning, exploratory analysis, feature engineering, model comparison, evaluation, and a reusable prediction pipeline for forecasting groundwater depth at monitoring stations.

This is the ML phase of the project only. The frontend, backend, APIs, and deployment work are intentionally left for future development.

## Project overview

The goal is to build a reliable predictive model for groundwater levels using historical station observations, temporal features, and spatial metadata. The workflow starts from raw monitoring data, performs cleaning and validation, creates engineered features, compares candidate regression models, and saves the best-performing model for reuse.

## Objectives

- Explore and validate the groundwater monitoring dataset.
- Clean duplicate, missing, and invalid observations.
- Understand temporal and station-wise patterns.
- Engineer features that capture seasonality, lag, and spatial context.
- Compare baseline and advanced regression models.
- Save the best model and use it in a reusable prediction pipeline.

## Dataset

The raw dataset is stored in:

- data/raw/Bengaluru_dataset.csv

The processed datasets used in the notebooks are stored in:

- data/processed/groundwater_cleaned.csv
- data/processed/groundwater_feature_engineered.csv

The dataset contains groundwater measurements from multiple monitoring stations with metadata such as station name, coordinates, timestamp, and RL_MSL values.

## Workflow

1. Data Exploration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Baseline Model
6. Model Training and Comparison
7. Model Evaluation
8. Spatial Analysis
9. Prediction Pipeline

## Feature engineering

Feature engineering includes station-based identifiers, temporal attributes, lag features, rolling statistics, and cyclical encodings for time-based patterns. These features help the model capture both short-term fluctuations and recurring seasonal behavior.

## Models

The project compares multiple regression approaches including:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

The best-performing model is saved to the models folder for later reuse.

## Evaluation

Model performance is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

The comparison is carried out on a chronological train/test split to preserve the time-series structure of the data.

## Prediction pipeline

The prediction pipeline loads the engineered dataset, prepares the feature matrix, loads the saved best model, and produces groundwater predictions for new feature rows. This keeps the workflow reusable without retraining the model unnecessarily.

## Folder structure

```text
groundwater-ai/
├── backend/                  # Future backend work; placeholder only
├── config/                   # Project configuration files
├── data/
│   ├── raw/
│   ├── processed/               
├── docs/                     # Documentation and notes
├── frontend/                 # Future frontend work; placeholder only
├── models/
│   ├── best_model.pkl
│   └── best_model_meta.json
├── notebooks/
├── src/
├── tests/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── .venv/                   # Local environment, not committed
```

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

The project dependencies are listed in `requirements.txt`.

## Results

The workflow identifies the best model using the engineered dataset and stores the trained artifact in the models directory. The saved pipeline supports consistent groundwater forecasting and future model reuse.

## Future work

Planned work beyond this ML phase includes:

- API and backend services
- Frontend dashboard and reporting
- Deployment and monitoring
- Operational data ingestion and retraining workflows

This repository intentionally keeps those areas separate so the core machine learning work remains focused and clean.
