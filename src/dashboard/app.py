import streamlit as st

from src.dashboard.queries import (
    get_predictions,
    get_dashboard_metrics
)
from src.monitoring.drift_monitor import get_drift_status


st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("🚨 Fraud Detection Dashboard")

metrics = get_dashboard_metrics()
drift_status = get_drift_status()


col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "Total Predictions",
    metrics["total_predictions"]
)

col2.metric(
    "Blocked",
    metrics["blocked"]
)

col3.metric(
    "Verified",
    metrics["verified"]
)

col4.metric(
    "Approved",
    metrics["approved"]
)

col5.metric(
    "Avg Fraud Probability",
    metrics["avg_probability"]
)
col6.metric(
    "Drift Status",
    drift_status
)


st.divider()

st.subheader("Recent Predictions")

df = get_predictions()

st.dataframe(
    df,
    use_container_width=True
)