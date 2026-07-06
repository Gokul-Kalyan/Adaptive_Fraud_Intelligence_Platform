import pandas as pd

from src.database.connection import get_connection


def get_predictions():

    connection = get_connection()

    query = """
        SELECT *
        FROM predictions
        ORDER BY timestamp DESC
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_dashboard_metrics():

    df = get_predictions()

    metrics = {
        "total_predictions": len(df),
        "blocked": len(df[df["decision"] == "BLOCK"]),
        "verified": len(df[df["decision"] == "VERIFY"]),
        "approved": len(df[df["decision"] == "APPROVE"]),
        "avg_probability": round(
            df["fraud_probability"].mean(),
            4
        )
        if not df.empty else 0
    }

    return metrics