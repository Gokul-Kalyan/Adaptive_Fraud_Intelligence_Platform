import pandas as pd

from src.database.connection import get_connection
from src.training.config import RAW_DATA_PATH


def get_training_data():

    df = pd.read_csv(RAW_DATA_PATH)

    return df


def get_production_data():

    connection = get_connection()

    query = """
        SELECT
            amount,
            transaction_type,
            fraud_probability,
            decision
        FROM predictions
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df