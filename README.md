# TikTok Trends Analysis Project

## Team Information

**Project Name:** TikTok Trends Analysis: Identifying Exploding Topics on TikTok

**Team Members:**
- Wenjing Huang - whuang08@usc.edu - GitHub: [your_github_username] - USC ID: [your_usc_id]

*Note: This is a single-person project.*

## Project Description

This project analyzes trending topics on TikTok by scraping data from Exploding Topics, a platform that tracks emerging trends. The goal is to identify the fastest-growing TikTok trends, understand their growth patterns, and visualize insights about what topics are currently exploding on the platform.

**Research Question:** What are the fastest-growing TikTok trends, and what patterns can we identify in their growth rates?

The project follows a complete data science pipeline:
1. **Data Collection**: Web scraping TikTok trends data from Exploding Topics
2. **Data Cleaning**: Extracting structured data from HTML and converting to CSV format
3. **Data Analysis**: Statistical analysis of growth rates and trend categorization
4. **Visualization**: Creating charts and graphs to communicate findings

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

This will install the following packages:
- `beautifulsoup4` - For parsing HTML content
- `requests` - For making HTTP requests to scrape web data
- `pandas` - For data manipulation and analysis
- `matplotlib` - For creating visualizations

## How to Run the Project

The project consists of three main scripts that should be run in sequence:

### Step 1: Data Collection (`get_data.py`)

This script scrapes TikTok trends data from Exploding Topics and saves the raw HTML file.

**Command:**
```bash
python src/get_data.py
```

**What it does:**
- Makes an HTTP GET request to `https://explodingtopics.com/blog/tiktok-trends`
- Uses browser-like headers to avoid being blocked
- Saves the raw HTML content to `data/raw/raw_tiktok_data.html`

**Expected output:**
```
Scraping https://explodingtopics.com/blog/tiktok-trends...
Success! Raw data saved to data/raw/raw_tiktok_data.html
```

### Step 2: Data Cleaning (`clean_data.py`)

This script processes the raw HTML file, extracts structured data from the trends table, and saves it as a cleaned CSV file.

**Command:**
```bash
python src/clean_data.py
```

**What it does:**
- Reads the raw HTML file from `data/raw/raw_tiktok_data.html`
- Parses the HTML using BeautifulSoup to locate the trends table
- Extracts three columns: rank, trend name, and growth percentage
- Cleans the data by converting growth percentages to numeric format
- Saves the cleaned data to `data/processed/cleaned_tiktok_data.csv`

**Expected output:**
```
Reading HTML from data/raw/raw_tiktok_data.html...
✓ Successfully cleaned data!
  - Found 51 TikTok trends
  - Saved to data/processed/cleaned_tiktok_data.csv

First 5 trends:
 rank            trend_name growth_percent  growth_numeric
  1.0           Roll On Oil        12,600%         12600.0
  2.0 Keyboard Cleaning Gel        10,500%         10500.0
  ...
```

### Step 3: Data Analysis and Visualization (`run_analysis.py`)

This script performs statistical analysis on the cleaned data and generates visualizations and reports.

**Command:**
```bash
python src/run_analysis.py
```

**What it does:**
- Reads the cleaned CSV file from `data/processed/cleaned_tiktok_data.csv`
- Calculates statistical summaries (mean, median, min, max growth rates)
- Categorizes trends by growth rate (high, medium, low)
- Generates three visualization files:
  - `results/top_10_trends.png` - Horizontal bar chart of top 10 fastest-growing trends
  - `results/growth_distribution.png` - Histogram showing distribution of growth rates
  - `results/top_5_trends.png` - Vertical bar chart of top 5 trends
- Creates a text report: `results/analysis_report.txt` with detailed statistics and findings

**Expected output:**
```
Reading cleaned data from data/processed/cleaned_tiktok_data.csv...

📊 Analysis Summary:
  - Total trends analyzed: 51
  - Mean growth: 1904.6%
  - Median growth: 1150.0%
  - Max growth: 12600.0%
  - Min growth: 734.0%
✓ Saved: results/top_10_trends.png
✓ Saved: results/growth_distribution.png
✓ Saved: results/top_5_trends.png
✓ Saved: results/analysis_report.txt

✅ Analysis complete! All results saved to results/ directory.
```

## Project Structure

```
my_project/
├── README.md                 # This file - project documentation
├── requirements.txt          # Python package dependencies
├── data/
│   ├── raw/                 # Raw data files (HTML from web scraping)
│   │   └── raw_tiktok_data.html
│   └── processed/           # Cleaned and structured data (CSV files)
│       └── cleaned_tiktok_data.csv
├── src/                     # Source code
│   ├── get_data.py         # Data collection script (web scraping)
│   ├── clean_data.py       # Data cleaning and preprocessing script
│   └── run_analysis.py     # Data analysis and visualization script
└── results/                 # Final outputs (reports and visualizations)
    ├── analysis_report.txt  # Text report with statistics
    ├── top_10_trends.png   # Visualization: Top 10 trends bar chart
    ├── growth_distribution.png  # Visualization: Growth rate histogram
    └── top_5_trends.png    # Visualization: Top 5 trends bar chart
```

## Data Sources

**Primary Data Source:**
- **Website**: Exploding Topics (https://explodingtopics.com/blog/tiktok-trends)
- **Data Type**: HTML table containing TikTok trends with growth percentages
- **Collection Method**: Web scraping using Python `requests` library
- **Number of Data Samples**: 51 TikTok trends

## Key Findings

Based on the analysis of 51 TikTok trends:
- **Top Trend**: Roll On Oil with 12,600% growth
- **Average Growth Rate**: 1,904.6%
- **Growth Distribution**: 
  - High growth (≥5,000%): 4 trends (7.8%)
  - Medium growth (1,000-5,000%): 26 trends (51.0%)
  - Low growth (<1,000%): 20 trends (39.2%)

## Troubleshooting

**Issue**: `ModuleNotFoundError` when running scripts
- **Solution**: Make sure you've activated your virtual environment and installed all requirements with `pip install -r requirements.txt`

**Issue**: `FileNotFoundError` when running `clean_data.py` or `run_analysis.py`
- **Solution**: Make sure you've run the previous scripts in sequence. `clean_data.py` requires `get_data.py` to run first, and `run_analysis.py` requires `clean_data.py` to run first.

**Issue**: Scripts run but produce no output
- **Solution**: Check that the website structure hasn't changed. The scraping script may need to be updated if Exploding Topics changes their HTML structure.

## Notes

- The `data/` directory may be ignored by git to avoid uploading large files. Make sure to run `get_data.py` before running other scripts.
- All visualizations are saved as PNG files with 300 DPI resolution for high-quality output.
- The analysis report includes detailed statistics and can be found in `results/analysis_report.txt`.

## License

This project is for educational purposes as part of DSCI 510: Principles of Programming for Data Science.
