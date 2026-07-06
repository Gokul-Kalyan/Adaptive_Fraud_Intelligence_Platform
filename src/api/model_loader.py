import joblib


MODEL_PATH = "models/catboost.pkl"


def load_model():

    model = joblib.load(MODEL_PATH)

    return model