import pandas as pd
import joblib

from catboost import CatBoostClassifier

from config import (
    RAW_DATA_PATH,
    TARGET_COLUMN,
    MODEL_PATH,
    RANDOM_STATE
)

from src.features.build_features import build_features


def load_data():

    df = pd.read_csv(RAW_DATA_PATH)

    return df


def prepare_dataset(df):

    df = build_features(df)

    X = df.drop(columns=[TARGET_COLUMN])

    y = df[TARGET_COLUMN]

    return X, y


def train_model(X_train, y_train):

    model = CatBoostClassifier(
        iterations=200,
        depth=6,
        learning_rate=0.1,
        random_seed=RANDOM_STATE,
        verbose=0,
        auto_class_weights="Balanced"
    )

    model.fit(X_train, y_train)

    return model


def save_model(model):

    joblib.dump(
        model,
        MODEL_PATH
    )

    print(f"Model saved to {MODEL_PATH}")

