"""
Web scraper script to collect HTML data.
Save HTML files to data/raw/ directory.
"""

import requests
import os

def get_data():
    # 1. The specific static URL
    url = "https://explodingtopics.com/blog/tiktok-trends"
    
    # Headers to look like a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Scraping {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check for errors

        # 2. Save raw HTML
        raw_path = os.path.join("data", "raw", "raw_tiktok_data.html")
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Success! Raw data saved to {raw_path}")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    get_data()