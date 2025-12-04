# Project README

## Team Information
[Add your team members' names and contact information here]

## Project Description
[Add a brief description of your project here]

## Instructions

### Setup
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the data collection script:
   ```bash
   python src/get_data.py
   ```

3. Clean the collected data:
   ```bash
   python src/clean_data.py
   ```

4. Run the analysis:
   ```bash
  python src/run_analysis.py
   ```

## Project Structure
- `data/raw/` - Raw HTML files from web scraping
- `data/processed/` - Clean CSV/JSON files
- `src/` - Source code for scraping, cleaning, and analysis
- `results/` - Final reports and figures

## Notes
- The `data/` directory is ignored by git to avoid uploading large files

