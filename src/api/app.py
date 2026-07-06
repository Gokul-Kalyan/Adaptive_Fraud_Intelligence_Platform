from fastapi import FastAPI

from src.api.model_loader import load_model
from src.api.schemas import TransactionRequest
from src.api.predict import prepare_request_features
from src.api.logger import log_prediction

app = FastAPI()

model = load_model()


@app.get("/")
def home():

    return {
        "message": "Fraud Detection API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict")
def predict(transaction: TransactionRequest):

    data = transaction.model_dump()

    features = prepare_request_features(data)

    probability = float(
        model.predict_proba(features)[0][1]
    )

    if probability >= 0.70:
        decision = "BLOCK"

    elif probability >= 0.30:
        decision = "VERIFY"

    else:
        decision = "APPROVE"

    # Log the prediction
    log_prediction(
        transaction=data,
        probability=probability,
        decision=decision
    )

    # Return prediction to the client
    return {
        "fraud_probability": round(
            probability,
            4
        ),
        "decision": decision
    }