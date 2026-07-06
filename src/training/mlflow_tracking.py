import mlflow
import mlflow.catboost

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("FraudDetection")


def log_experiment(
    model,
    params,
    metrics
):

    with mlflow.start_run():

        for key, value in params.items():
            mlflow.log_param(
                key,
                value
            )

        for key, value in metrics.items():
            mlflow.log_metric(
                key,
                value
            )

        mlflow.catboost.log_model(
            cb_model=model,
            name="fraud_detector_model"
        )