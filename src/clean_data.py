"""
Data cleaning script.
Read HTML files from data/raw/ and save clean CSV/JSON to data/processed/.
"""

import pandas as pd
from bs4 import BeautifulSoup
import os
import re

def clean_data():
    raw_path = os.path.join("data", "raw", "raw_tiktok_data.html")
    
    if not os.path.exists(raw_path):
        print("Error: Raw data file not found. Run get_data.py first!")
        return

    print(f"Reading HTML from {raw_path}...")
    with open(raw_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    trends = []
    
    # Find the table containing the trends data
    table = soup.find("table")
    
    if not table:
        print("Error: Could not find table in HTML. The page structure may have changed.")
        return
    
    # Extract data from table rows (skip header row if present)
    rows = table.find_all("tr")
    
    for row in rows:
        cells = row.find_all("td")
        
        # Each row should have 3 columns: rank, trend_name, growth_percent
        if len(cells) >= 3:
            rank = cells[0].get_text(strip=True)
            trend_name = cells[1].get_text(strip=True)
            growth_percent = cells[2].get_text(strip=True)
            
            trends.append({
                "rank": rank,
                "trend_name": trend_name,
                "growth_percent": growth_percent
            })

    # Create DataFrame
    df = pd.DataFrame(trends)
    
    if df.empty:
        print("Warning: No trends data extracted. Check the HTML structure.")
        return
    
    # Basic Cleaning
    # Convert rank to numeric
    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
    
    # Clean growth_percent: remove commas and % sign, convert to numeric
    df['growth_numeric'] = df['growth_percent'].str.replace(',', '').str.replace('%', '')
    df['growth_numeric'] = pd.to_numeric(df['growth_numeric'], errors='coerce')
    
    # Sort by rank to ensure proper ordering
    df = df.sort_values('rank').reset_index(drop=True)

    # Save to CSV
    out_path = os.path.join("data", "processed", "cleaned_tiktok_data.csv")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    
    print(f"✓ Successfully cleaned data!")
    print(f"  - Found {len(df)} TikTok trends")
    print(f"  - Saved to {out_path}")
    print(f"\nFirst 5 trends:")
    print(df.head().to_string(index=False))

if __name__ == "__main__":
    clean_data()