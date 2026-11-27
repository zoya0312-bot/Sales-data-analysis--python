# Sales Data Analysis Using Python

An end-to-end data analysis project built with Python, Pandas, NumPy, and Matplotlib to merge 12 monthly sales CSV files, clean missing and malformed records, and extract actionable business insights.

## Objectives
- Combine multiple monthly sales CSV files into a single dataset.
- Clean missing values, fix data types, and engineer features (`Month`, `Sales`, `City`).
- Analyse monthly revenue trends, city-wise sales performance, and top-selling products.
- Visualise findings using Matplotlib.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib

## Project Files
- `generate_data.py` — Generates 12 monthly sales CSV files with realistic transactions and missing values.
- `sales_analysis.py` — Merges, cleans, analyses the dataset, and generates visualisations.
- `monthly_sales.png` — Monthly sales revenue chart.
- `sales_by_city.png` — Total sales by city chart.
- `top_products.png` — Top-selling products by quantity sold.

## How to Run
1. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib
