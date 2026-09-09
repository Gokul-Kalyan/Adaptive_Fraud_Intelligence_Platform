# Adaptive Fraud Intelligence Platform

An end-to-end machine learning platform for fraud detection, designed to identify high-risk transactions while supporting model experimentation, API-based inference, monitoring, and business-impact analysis.

## Key Result

**F1 Score: 95.2%**

The project combines machine learning with production-oriented engineering to demonstrate the complete workflow from data processing and model development to deployment and monitoring.

---

## Project Overview

Fraud detection is a highly imbalanced classification problem where missing fraudulent transactions can have significant business impact.

This project focuses on building a practical fraud detection system that can:

- Process transaction data
- Perform feature engineering and preprocessing
- Train and evaluate machine learning models
- Track experiments using MLflow
- Serve predictions through a FastAPI service
- Provide an interactive dashboard
- Store application data using PostgreSQL
- Run the system using Docker
- Monitor model/data behavior for potential drift
- Analyze the business impact of fraud predictions

---

## Machine Learning Approach

### Model

**CatBoost Classifier**

CatBoost was selected as the primary model because of its strong performance on tabular data, well adaptable for handling categorical variables and its ability to capture nonlinear relationships with relatively limited preprocessing. 

### Evaluation

Because fraud detection is an imbalanced classification problem, accuracy alone is not an appropriate measure of model performance.

The primary evaluation metric is:

**F1 Score: 95.2%**

F1 balances precision and recall and provides a more useful view of performance when both false positives and false negatives matter.

Additional evaluation includes classification metrics and analysis of prediction errors.

---

## End-to-End Architecture

```text
Transaction Data
       |
       v
Data Preprocessing
       |
       v
Feature Engineering
       |
       v
CatBoost Model
       |
       v
Model Evaluation
       |
       +--------------------+
       |                    |
       v                    v
     MLflow              Model Artifact
       |                    |
       |                    v
       |                FastAPI
       |                    |
       |                    v
       |               Predictions
       |                    |
       +----------+---------+
                  |
                  v
             Dashboard
                  |
                  v
        Monitoring & Analytics
