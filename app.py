from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="MTL PCGrad Dashboard", layout="wide")
st.title("Multi-Task Learning with Gradient Surgery (PCGrad)")

RESULTS = Path("results")


def load_csv(name: str) -> pd.DataFrame | None:
    path = RESULTS / name
    if not path.exists():
        st.warning(f"Missing required file: {path}")
        return None
    return pd.read_csv(path)


grad_df = load_csv("gradient_conflict.csv")
baseline_df = load_csv("baseline_metrics.csv")
pcgrad_df = load_csv("pcgrad_metrics.csv")
repr_df = load_csv("representation_projection.csv")

st.markdown('<div data-testid="gradient-conflict-monitor"></div>', unsafe_allow_html=True)
st.subheader("Gradient Conflict Monitor")
if grad_df is not None and not grad_df.empty:
    fig_conflict = px.line(grad_df, x="step", y="cosine_similarity", title="Cosine Similarity Between Task Gradients")
    fig_conflict.add_hline(y=0.0, line_dash="dash", line_color="red")
    st.plotly_chart(fig_conflict, use_container_width=True)

st.markdown('<div data-testid="performance-dashboard"></div>', unsafe_allow_html=True)
st.subheader("Performance Dashboard")
if baseline_df is not None and pcgrad_df is not None:
    merged = baseline_df.merge(pcgrad_df, on="epoch", suffixes=("_baseline", "_pcgrad"))

    c1, c2 = st.columns(2)
    with c1:
        fig_a = px.line(
            merged,
            x="epoch",
            y=["val_task_a_accuracy_baseline", "val_task_a_accuracy_pcgrad"],
            title="Task A Validation Accuracy",
        )
        st.plotly_chart(fig_a, use_container_width=True)

    with c2:
        fig_b = px.line(
            merged,
            x="epoch",
            y=["val_task_b_accuracy_baseline", "val_task_b_accuracy_pcgrad"],
            title="Task B Validation Accuracy",
        )
        st.plotly_chart(fig_b, use_container_width=True)

st.markdown('<div data-testid="representation-inspector"></div>', unsafe_allow_html=True)
st.subheader("Shared Representation Inspector (2D Projection)")
if repr_df is not None and not repr_df.empty:
    color_by = st.radio("Color points by", ["task_a", "task_b"], horizontal=True)
    fig_repr = px.scatter(
        repr_df,
        x="dim1",
        y="dim2",
        color=repr_df[color_by].astype(str),
        title=f"Shared Representation colored by {color_by}",
        opacity=0.7,
    )
    st.plotly_chart(fig_repr, use_container_width=True)
