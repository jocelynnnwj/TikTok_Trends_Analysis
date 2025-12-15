"""
Analysis script.
Read cleaned data from data/processed/ and generate results/figures.
Save final reports and figures to results/ directory.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def analyze():
    data_path = os.path.join("data", "processed", "cleaned_tiktok_data.csv")
    if not os.path.exists(data_path):
        print("Error: Processed data not found. Run clean_data.py first!")
        return

    print(f"Reading cleaned data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)
    
    # Basic statistics
    total_trends = len(df)
    mean_growth = df['growth_numeric'].mean()
    median_growth = df['growth_numeric'].median()
    max_growth = df['growth_numeric'].max()
    min_growth = df['growth_numeric'].min()
    
    print(f"\n📊 Analysis Summary:")
    print(f"  - Total trends analyzed: {total_trends}")
    print(f"  - Mean growth: {mean_growth:.1f}%")
    print(f"  - Median growth: {median_growth:.1f}%")
    print(f"  - Max growth: {max_growth:.1f}%")
    print(f"  - Min growth: {min_growth:.1f}%")
    
    # 1. Top 10 Fastest Growing Trends - Horizontal Bar Chart
    top_10 = df.nlargest(10, 'growth_numeric')
    
    plt.figure(figsize=(12, 8))
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(top_10)))
    bars = plt.barh(range(len(top_10)), top_10['growth_numeric'], color=colors)
    plt.yticks(range(len(top_10)), top_10['trend_name'])
    plt.xlabel('Growth Percentage (%)', fontsize=12, fontweight='bold')
    plt.title('Top 10 Fastest Growing TikTok Trends', fontsize=14, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()  # Highest on top
    
    # Add value labels on bars
    for i, (idx, row) in enumerate(top_10.iterrows()):
        plt.text(row['growth_numeric'] + 50, i, f"{row['growth_numeric']:,.0f}%", 
                va='center', fontsize=9)
    
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    save_path = os.path.join("results", "top_10_trends.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {save_path}")
    
    # 2. Growth Distribution Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['growth_numeric'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Growth Percentage (%)', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Trends', fontsize=12, fontweight='bold')
    plt.title('Distribution of TikTok Trend Growth Rates', fontsize=14, fontweight='bold', pad=20)
    plt.axvline(mean_growth, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_growth:.1f}%')
    plt.axvline(median_growth, color='green', linestyle='--', linewidth=2, label=f'Median: {median_growth:.1f}%')
    plt.legend()
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    save_path = os.path.join("results", "growth_distribution.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {save_path}")
    
    # 3. Top 5 Trends - Simple Bar Chart
    top_5 = df.nlargest(5, 'growth_numeric')
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(top_5)), top_5['growth_numeric'], 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
    plt.xticks(range(len(top_5)), top_5['trend_name'], rotation=45, ha='right')
    plt.ylabel('Growth Percentage (%)', fontsize=12, fontweight='bold')
    plt.title('Top 5 Exploding TikTok Trends', fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels on top of bars
    for i, (idx, row) in enumerate(top_5.iterrows()):
        plt.text(i, row['growth_numeric'] + 100, f"{row['growth_numeric']:,.0f}%", 
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    save_path = os.path.join("results", "top_5_trends.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {save_path}")
    
    # 4. Generate comprehensive text report
    report_path = os.path.join("results", "analysis_report.txt")
    with open(report_path, "w") as f:
        f.write("=" * 70 + "\n")
        f.write("TIKTOK TRENDS ANALYSIS REPORT\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("OVERVIEW\n")
        f.write("-" * 70 + "\n")
        f.write(f"Total Trends Analyzed: {total_trends}\n")
        f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("STATISTICAL SUMMARY\n")
        f.write("-" * 70 + "\n")
        f.write(f"Mean Growth Rate:     {mean_growth:,.1f}%\n")
        f.write(f"Median Growth Rate:   {median_growth:,.1f}%\n")
        f.write(f"Maximum Growth Rate:  {max_growth:,.1f}%\n")
        f.write(f"Minimum Growth Rate:  {min_growth:,.1f}%\n")
        f.write(f"Standard Deviation:   {df['growth_numeric'].std():,.1f}%\n\n")
        
        f.write("TOP 10 FASTEST GROWING TRENDS\n")
        f.write("-" * 70 + "\n")
        for idx, row in top_10.iterrows():
            f.write(f"{int(row['rank']):2d}. {row['trend_name']:<40} {row['growth_percent']:>10}\n")
        f.write("\n")
        
        f.write("GROWTH CATEGORIES\n")
        f.write("-" * 70 + "\n")
        high_growth = len(df[df['growth_numeric'] >= 5000])
        medium_growth = len(df[(df['growth_numeric'] >= 1000) & (df['growth_numeric'] < 5000)])
        low_growth = len(df[df['growth_numeric'] < 1000])
        
        f.write(f"High Growth (≥5,000%):     {high_growth:3d} trends ({high_growth/total_trends*100:.1f}%)\n")
        f.write(f"Medium Growth (1,000-5,000%): {medium_growth:3d} trends ({medium_growth/total_trends*100:.1f}%)\n")
        f.write(f"Low Growth (<1,000%):      {low_growth:3d} trends ({low_growth/total_trends*100:.1f}%)\n\n")
        
        f.write("=" * 70 + "\n")
        f.write("Report generated by run_analysis.py\n")
        f.write("=" * 70 + "\n")
    
    print(f"✓ Saved: {report_path}")
    
    print(f"\n✅ Analysis complete! All results saved to results/ directory.")
    print(f"\nGenerated files:")
    print(f"  - top_10_trends.png (bar chart)")
    print(f"  - growth_distribution.png (histogram)")
    print(f"  - top_5_trends.png (bar chart)")
    print(f"  - analysis_report.txt (text report)")

if __name__ == "__main__":
    analyze()