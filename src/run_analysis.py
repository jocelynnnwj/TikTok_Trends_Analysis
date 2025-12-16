"""
Analysis Script.
Performs statistical analysis on 50,000+ rows.
Generates:
1. Virality Scatter Plot (Views vs Likes)
2. Correlation Heatmap
3. Statistical Summary Report
"""

import os
from datetime import datetime

import pandas as pd

from visualize_results import create_visualizations

def generate_report(df):
    report_path = os.path.join("results", "analysis_report.txt")
    
    with open(report_path, "w") as f:
        f.write("="*60 + "\n")
        f.write("BIG DATA ANALYSIS REPORT: TIKTOK TRENDS 2025\n")
        f.write("="*60 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("DATASET SUMMARY\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Samples Analyzed: {len(df):,}\n")
        f.write(f"Data Source: Kaggle API (YouTube Shorts & TikTok Trends)\n\n")
        
        f.write("ENGAGEMENT STATISTICS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Average Views:    {df['view_count'].mean():,.0f}\n")
        f.write(f"Median Views:     {df['view_count'].median():,.0f}\n")
        f.write(f"Max Views:        {df['view_count'].max():,.0f}\n")
        f.write(f"Average Likes:    {df['like_count'].mean():,.0f}\n")
        f.write(f"Max Likes:        {df['like_count'].max():,.0f}\n\n")
        
        f.write("INSIGHTS\n")
        f.write("-" * 30 + "\n")
        # Calculate simplistic "Viral Ratio" (Likes / Views)
        df['engagement_rate'] = df['like_count'] / df['view_count']
        avg_rate = df['engagement_rate'].mean() * 100
        f.write(f"Average Engagement Rate: {avg_rate:.2f}%\n")
        
    print(f"📝 Report saved to: {report_path}")

def analyze():
    data_path = os.path.join("data", "processed", "cleaned_tiktok_trends.csv")
    
    if not os.path.exists(data_path):
        print("❌ No data found. Run clean_data.py first!")
        return
        
    print("📊 Loading processed data...")
    df = pd.read_csv(data_path)
    print(f"   Loaded {len(df)} rows.")
    
    create_visualizations(df)
    generate_report(df)
    print("\n✅ Analysis Pipeline Complete!")

if __name__ == "__main__":
    analyze()