"""
Data Collection Script.
Uses Kaggle API (via kagglehub) to download the
'YouTube Shorts and TikTok Trends 2025' dataset from Kaggle.

NOTE: For security, Kaggle credentials are NOT hard-coded.
Set these in your environment before running:
  - KAGGLE_USERNAME
  - KAGGLE_API_TOKEN  (or KAGGLE_KEY, depending on your setup)
"""

import kagglehub
import shutil
import os


def get_data():
    # --- 1. AUTHENTICATION (via environment variables) ---
    username = os.environ.get("KAGGLE_USERNAME")
    token = os.environ.get("KAGGLE_API_TOKEN") or os.environ.get("KAGGLE_KEY")

    if not username or not token:
        print("❌ Kaggle credentials not found.")
        print("   Please set KAGGLE_USERNAME and KAGGLE_API_TOKEN (or KAGGLE_KEY) in your environment.")
        print("   Example (macOS/Linux):")
        print("     export KAGGLE_USERNAME='your_username'")
        print("     export KAGGLE_API_TOKEN='your_token'")
        return

    print("🚀 Authenticating with Kaggle via environment variables...")

    try:
        # --- 2. DOWNLOAD DATASET ---
        print("📥 Downloading 'YouTube Shorts and TikTok Trends 2025'...")
        # This downloads the files to a local cache folder
        path = kagglehub.dataset_download(
            "tarekmasryo/youtube-shorts-and-tiktok-trends-2025"
        )
        print(f"✅ Download complete! Cache path: {path}")

        # --- 3. MOVE TO PROJECT FOLDER ---
        target_dir = os.path.join("data", "raw")
        os.makedirs(target_dir, exist_ok=True)

        # Look for the CSV in the downloaded files
        files = os.listdir(path)
        csv_found = False

        for file in files:
            if file.endswith(".csv"):
                source_file = os.path.join(path, file)
                # Rename to a standard name for our pipeline
                dest_file = os.path.join(target_dir, "raw_tiktok_trends.csv")
                shutil.copy(source_file, dest_file)
                print(f"📦 Moved data to project: {dest_file}")
                csv_found = True
                break

        if not csv_found:
            print("❌ Error: No CSV file found in the download.")

    except Exception as e:
        print(f"❌ Error during download: {e}")
        print("Tip: Ensure 'kagglehub' is installed (pip install kagglehub)")


if __name__ == "__main__":
    get_data()