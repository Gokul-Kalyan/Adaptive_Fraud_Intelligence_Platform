import pandas as pd


def prepare_request_features(data):

    df = pd.DataFrame([data])

    mapping = {
        "PAYMENT": 0,
        "TRANSFER": 1,
        "CASH_OUT": 2,
        "DEBIT": 3,
        "CASH_IN": 4
    }

    df["type"] = df["type"].map(mapping)

    df["balance_diff_org"] = (
        df["oldbalanceOrg"]
        - df["newbalanceOrig"]
    )

    df["balance_diff_dest"] = (
        df["newbalanceDest"]
        - df["oldbalanceDest"]
    )

    df["amount_balance_ratio"] = (
        df["amount"]
        / (df["oldbalanceOrg"] + 1)
    )

    df["full_balance_transfer"] = (
        df["amount"]
        >= df["oldbalanceOrg"] * 0.95
    ).astype(int)

    return df