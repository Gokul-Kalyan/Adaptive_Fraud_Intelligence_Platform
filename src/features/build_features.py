import pandas as pd


def clean_data(df):
    """
    Remove columns not useful for fraud prediction.
    """

    columns_to_drop = [
        "nameOrig",
        "nameDest",
        "isFlaggedFraud"
    ]

    df = df.drop(columns=columns_to_drop)

    return df


def encode_transaction_type(df):
    """
    Convert transaction type into numerical values.
    """

    mapping = {
        "PAYMENT": 0,
        "TRANSFER": 1,
        "CASH_OUT": 2,
        "DEBIT": 3,
        "CASH_IN": 4
    }

    df["type"] = df["type"].map(mapping)

    return df


def create_balance_features(df):

    df["balance_diff_org"] = (
        df["oldbalanceOrg"]
        - df["newbalanceOrig"]
    )

    df["balance_diff_dest"] = (
        df["newbalanceDest"]
        - df["oldbalanceDest"]
    )

    return df


def create_ratio_features(df):

    df["amount_balance_ratio"] = (
        df["amount"]
        / (df["oldbalanceOrg"] + 1)
    )

    return df


def create_transfer_flags(df):

    df["full_balance_transfer"] = (
        df["amount"]
        >= df["oldbalanceOrg"] * 0.95
    ).astype(int)

    return df


def build_features(df):

    df = clean_data(df)

    df = encode_transaction_type(df)

    df = create_balance_features(df)

    df = create_ratio_features(df)

    df = create_transfer_flags(df)

    return df