from src.api.logger import log_prediction

transaction = {
    "amount": 100000,
    "type": "TRANSFER"
}

log_prediction(
    transaction=transaction,
    probability=0.98,
    decision="BLOCK"
)

print("✅ Prediction logged successfully!")