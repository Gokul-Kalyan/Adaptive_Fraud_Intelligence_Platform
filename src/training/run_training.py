from sklearn.model_selection import train_test_split

from config import RANDOM_STATE

from src.training.mlflow_tracking import (
    log_experiment
)

from src.training.train import (
    load_data,
    prepare_dataset,
    train_model,
    save_model
)

from src.training.evaluate import (
    evaluate_model
)


def main():

    print("Loading data...")

    df = load_data()

    print("Building features...")

    X, y = prepare_dataset(df)

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("Training CatBoost...")

    model = train_model(
        X_train,
        y_train
    )

    print("Evaluating Model...")

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    params = {
        "iterations": 200,
        "depth": 6,
        "learning_rate": 0.1
    }

    log_experiment (
    model,
    params,
    metrics
)

    save_model(model)

    print("Pipeline Complete")


if __name__ == "__main__":
    main()