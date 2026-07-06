import pandas as pd

from scipy.stats import ks_2samp

from src.database.connection import get_connection


TRAINING_DATA_PATH = "data/raw/fraud.csv"


def load_training_data():

    df = pd.read_csv(
        TRAINING_DATA_PATH,
        usecols=["amount"]
    )

    return df


def load_production_data():

    connection = get_connection()

    query = """
        SELECT amount
        FROM predictions
        WHERE amount IS NOT NULL
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def detect_amount_drift():

    train_df = load_training_data()

    prod_df = load_production_data()

    if len(prod_df) < 5:

        return {
            "status": "NOT ENOUGH DATA",
            "message": "Need at least 5 production predictions."
        }

    statistic, p_value = ks_2samp(
        train_df["amount"],
        prod_df["amount"]
    )

    drift_detected = p_value < 0.05

    return {
        "training_records": len(train_df),
        "production_records": len(prod_df),
        "ks_statistic": round(statistic, 4),
        "p_value": round(p_value, 4),
        "drift_detected": drift_detected,
        "status": "DRIFT DETECTED" if drift_detected else "NO DRIFT"
    }
def get_drift_status():
    result = detect_amount_drift()

    if result["status"] == "NO DRIFT":
        return "🟢 NO DRIFT"

    elif result["status"] == "DRIFT DETECTED":
        return "🔴 DRIFT DETECTED"

    else:
        return "🟡 NOT ENOUGH DATA"


if __name__ == "__main__":

    result = detect_amount_drift()

    print("\n===== DRIFT REPORT =====")

    for key, value in result.items():
        print(f"{key}: {value}")