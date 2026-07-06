import joblib

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

from config import MODEL_PATH


def load_model():

    model = joblib.load(MODEL_PATH)

    return model


def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"\nPrecision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    metrics = {
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }

    return metrics