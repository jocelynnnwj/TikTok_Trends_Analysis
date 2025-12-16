"""
Data Cleaning Script.
Processes the Kaggle CSV and normalizes columns for analysis.
- Renames and coerces numeric fields
- Estimates like_count from engagement rate when likes are absent
"""

import pandas as pd
import os


def clean_data():
    raw_path = os.path.join("data", "raw", "raw_tiktok_trends.csv")

    if not os.path.exists(raw_path):
        print("❌ Run get_data.py first!")
        return

    print("🧹 Loading dataset...")

    try:
        df = pd.read_csv(raw_path, on_bad_lines="skip")
    except Exception:
        df = pd.read_csv(raw_path)

    print(f"   Raw shape: {df.shape}")

    # Expected Kaggle columns: ['country', 'platform', 'year_month', 'n_videos', 'views', 'avg_er', 'avg_velocity', 'trend_label']
    # Normalize column names for downstream analysis
    rename_map = {
        "views": "view_count",
        "avg_er": "engagement_rate",
        "avg_velocity": "velocity",
    }
    df = df.rename(columns=rename_map)

    # Coerce numeric columns
    numeric_cols = ["view_count", "engagement_rate", "velocity", "n_videos"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where view_count or engagement_rate is missing
    df.dropna(subset=["view_count", "engagement_rate"], inplace=True)

    # Remove zero or negative views
    df = df[df["view_count"] > 0]

    # If like_count is not present, estimate likes from engagement_rate (assumed fractional)
    if "like_count" not in df.columns:
        df["like_count"] = df["view_count"] * df["engagement_rate"]

    # Drop rows with missing like_count after estimation
    df.dropna(subset=["like_count"], inplace=True)

    # Save processed data
    out_dir = os.path.join("data", "processed")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cleaned_tiktok_trends.csv")

    df.to_csv(out_path, index=False)

    print("✅ Cleaning complete!")
    print(f"   Final Dataset Size: {len(df)} rows")
    print(f"   Saved to: {out_path}")


if __name__ == "__main__":
    clean_data()