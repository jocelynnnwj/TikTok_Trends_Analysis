# TikTok Trends Analysis Project

**Wenjing Huang** | whuang08@usc.edu | USC ID: 3860016877

## Project Description

This project performs an exploratory analysis of short‑form video performance using the Kaggle dataset **"YouTube Shorts and TikTok Trends 2025"**. The goal is to understand how view counts and like counts relate to each other and to summarize engagement behavior across thousands of viral clips.

**Research Question:** What does the relationship between views and likes look like for highly viewed short‑form videos, and what is the typical engagement rate across the dataset?

The project follows a compact but complete data science pipeline:
1. **Data Collection**: Downloading the Kaggle dataset using the Kaggle API (via `kagglehub`)
2. **Data Cleaning**: Normalizing column names, coercing numeric fields, filtering invalid rows, and constructing a `like_count` column when necessary
3. **Data Analysis & Visualization**: Summarizing engagement statistics and generating visualizations for virality and correlations between numeric metrics

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Create a Virtual Environment

It is recommended to use a virtual environment to isolate project dependencies:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Required Libraries

Once your virtual environment is activated, install all required dependencies:

```bash
pip install -r requirements.txt
```

This will install the following packages (key ones listed):
- `kagglehub` - For downloading datasets from Kaggle using the Kaggle API
- `pandas` - For data manipulation and analysis
- `matplotlib` - For creating visualizations
- `seaborn` - For enhanced visualization styling
- `requests`, `beautifulsoup4` - Included for potential future web requests / parsing

## How to Run the Project

The project consists of three main scripts that should be run in sequence.

### Step 1: Data Collection (`get_data.py`)

This script downloads the **YouTube Shorts and TikTok Trends 2025** dataset from Kaggle.

Before running it, set your Kaggle credentials in the environment:

```bash
export KAGGLE_USERNAME="your_username"
export KAGGLE_API_TOKEN="your_token"
```

On Windows (PowerShell), you can use:

```powershell
$env:KAGGLE_USERNAME="your_username"
$env:KAGGLE_API_TOKEN="your_token"
```

**Command:**
```bash
python src/get_data.py
```

**What it does:**
- Authenticates with Kaggle using `KAGGLE_USERNAME` and `KAGGLE_API_TOKEN`
- Downloads the dataset via `kagglehub.dataset_download`
- Copies the main CSV file into `data/raw/` as `raw_tiktok_trends.csv`

**Expected output (abridged):**

```text
🚀 Authenticating with Kaggle via environment variables...
📥 Downloading 'YouTube Shorts and TikTok Trends 2025'...
✅ Download complete! Cache path: ...
📦 Moved data to project: data/raw/raw_tiktok_trends.csv
```

### Step 2: Data Cleaning (`clean_data.py`)

This script processes the raw CSV file from Kaggle and prepares a clean dataset for analysis.

**Command:**
```bash
python src/clean_data.py
```

**What it does:**
- Loads `data/raw/raw_tiktok_trends.csv`
- Renames key columns (e.g., `views` → `view_count`, `avg_er` → `engagement_rate`, `avg_velocity` → `velocity`)
- Coerces numeric columns (`view_count`, `engagement_rate`, `velocity`, `n_videos`)
- Drops rows with missing or invalid `view_count` / `engagement_rate`
- Ensures strictly positive `view_count`
- Creates a `like_count` column if it does not exist (estimated as `view_count * engagement_rate`)
- Saves a single cleaned dataset:
  - `data/processed/cleaned_tiktok_trends.csv`

**Expected output (abridged):**

```text
🧹 Loading dataset...
   Raw shape: (N, 8)
✅ Cleaning complete!
   Final Dataset Size: M rows
   Saved to: data/processed/cleaned_tiktok_trends.csv
```

### Step 3: Data Analysis and Visualization (`run_analysis.py` + `visualize_results.py`)

This step reads the cleaned dataset, generates visualizations, and writes a concise text report.

**Command:**
```bash
python src/run_analysis.py
```

**What it does:**
- Reads `data/processed/cleaned_tiktok_trends.csv`
- Uses `visualize_results.create_visualizations(df)` to generate:
  - `results/virality_scatter.png` – log–log scatter of `view_count` vs `like_count`
  - `results/correlation_heatmap.png` – correlation heatmap of numeric features
- Computes summary engagement statistics and writes:
  - `results/analysis_report.txt`
  
**Note:** The final comprehensive report (`results/final_report.pdf`) is a LaTeX-generated PDF document that provides a detailed analysis of the findings. This PDF is created separately and should be placed in the `results/` folder.

**Expected output (abridged):**

```text
📊 Loading processed data...
   Loaded M rows.
🎨 Generating Scatter Plot...
🎨 Generating Correlation Heatmap...
📝 Report saved to: results/analysis_report.txt

✅ Analysis Pipeline Complete!
```

## Project Structure

```text
TikTok_Trends_Analysis/
├── README.md                  # This file - project documentation
├── requirements.txt           # Python package dependencies
├── .gitignore                 # Git ignore file
├── project_proposal.pdf       # Project proposal document
├── data/
│   ├── raw/                   # Raw data files from Kaggle
│   │   └── raw_tiktok_trends.csv
│   └── processed/             # Cleaned and structured data (CSV files)
│       └── cleaned_tiktok_trends.csv
├── src/                       # Source code
│   ├── get_data.py            # Data collection script (Kaggle download)
│   ├── clean_data.py          # Data cleaning script for the Kaggle CSV
│   ├── run_analysis.py        # Analysis + text report generation
│   ├── visualize_results.py   # Visualization utilities (plots saved to results/)
│   └── utils/                 # Utility package (placeholder for shared helpers)
│       └── __init__.py
└── results/                   # Final outputs (reports and visualizations)
    ├── analysis_report.txt    # Engagement summary report
    ├── final_report.pdf       # Final analysis report (LaTeX/PDF)
    ├── correlation_heatmap.png
    └── virality_scatter.png
```

## Data Source

**Primary Dataset:**

1. **YouTube Shorts and TikTok Trends 2025 (Kaggle)**
   - **Host**: Kaggle
   - **Access Method**: Kaggle API via `kagglehub`
   - **Data Type**: CSV file with aggregated metrics for trending short‑form videos
   - **Example Fields**: `country`, `platform`, `year_month`, `n_videos`, `views`, `avg_er`, `avg_velocity`, `trend_label`

During cleaning, these are normalized into analysis‑friendly fields such as `view_count`, `engagement_rate`, `velocity`, `n_videos`, and `like_count`.

## Troubleshooting

**Issue**: `ModuleNotFoundError` when running scripts  
- **Solution**: Make sure you've activated your virtual environment and installed all requirements with `pip install -r requirements.txt`.

**Issue**: `FileNotFoundError` when running `clean_data.py` or `run_analysis.py`  
- **Solution**: Make sure you've run the previous scripts in sequence. `clean_data.py` requires `get_data.py` to run first, and `run_analysis.py` requires `clean_data.py` to run first.

**Issue**: Kaggle credentials error in `get_data.py`  
- **Solution**: Confirm that `KAGGLE_USERNAME` and `KAGGLE_API_TOKEN` (or `KAGGLE_KEY`) are set in your environment and match your Kaggle account settings.

**Issue**: Warning about `~/.matplotlib` not being writable when running `run_analysis.py`  
- **Solution**: Set the `MPLCONFIGDIR` environment variable to a writable directory, for example:

```bash
export MPLCONFIGDIR=/tmp/mplcache
```

**Issue**: `ModuleNotFoundError: No module named 'seaborn'`  
- **Solution**: Install Seaborn with `pip install seaborn`.

## Notes

- The project uses a single Kaggle dataset as its primary source.
- Data cleaning focuses on ensuring numeric correctness and constructing a consistent `like_count` metric.
- Visualizations are saved as PNG files with 300 DPI resolution for high-quality output.
- The analysis report (`analysis_report.txt`) includes key descriptive statistics and an approximate engagement rate.
- The project proposal (`project_proposal.pdf`) outlines the initial research plan and methodology.
- The final report (`results/final_report.pdf`) provides a comprehensive LaTeX-formatted analysis of the findings.

## License

This project is for educational purposes as part of DSCI 510: Principles of Programming for Data Science.
