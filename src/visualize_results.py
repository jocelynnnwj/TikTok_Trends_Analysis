"""
Visualization utilities for the TikTok trends analysis project.

This module is responsible only for generating plots and saving them
to the `results/` directory. Analytical/reporting logic lives in
`run_analysis.py`.
"""

import os

import matplotlib.pyplot as plt
import seaborn as sns


# Set style for professional plots (kept consistent with run_analysis)
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 300


def create_visualizations(df):
    """
    Generate and save all figures used in the final report.

    Currently produces:
    - Virality scatter plot (views vs likes) on log–log scale
    - Correlation heatmap for numeric engagement metrics
    """
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)

    # --- VIZ 1: VIRALITY SCATTER PLOT (The "Viral Curve") ---
    print("🎨 Generating Scatter Plot...")
    plt.figure(figsize=(10, 6))

    # We use alpha blending because tens of thousands of dots can get messy
    sns.scatterplot(
        data=df,
        x="view_count",
        y="like_count",
        alpha=0.4,
        color="#ff0050",  # TikTok Red
        edgecolor=None,
    )

    plt.title(
        "Virality Analysis: Relationship Between Views and Likes",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Views (Log Scale)", fontsize=12)
    plt.ylabel("Likes (Log Scale)", fontsize=12)

    # Log scale is crucial for social media data
    plt.xscale("log")
    plt.yscale("log")

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "virality_scatter.png"))
    plt.close()

    # --- VIZ 2: CORRELATION HEATMAP ---
    print("🎨 Generating Correlation Heatmap...")
    plt.figure(figsize=(8, 6))

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["float64", "int64"])
    corr_matrix = numeric_df.corr()

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )

    plt.title("Correlation of Engagement Metrics", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
    plt.close()

