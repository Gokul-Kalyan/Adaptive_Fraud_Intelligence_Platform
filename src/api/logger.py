from datetime import datetime

from src.database.connection import get_connection


def log_prediction(
    transaction,
    probability,
    decision
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (
            timestamp,
            amount,
            transaction_type,
            fraud_probability,
            decision
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            datetime.now(),
            transaction["amount"],
            transaction["type"],
            round(probability, 4),
            decision
        )
    )

    connection.commit()

    cursor.close()

    connection.close()