import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Combine all 12 monthly CSV files
csv_files = sorted(glob.glob("sales_data/*.csv"))
df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)
print(f"Combined {len(csv_files)} files. Initial shape: {df.shape}")

# 2. Data Cleaning
df = df.dropna(how="any").copy()
df = df[df["Order Date"].str[:2] != "Or"]

df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors="coerce")
df["Price Each"] = pd.to_numeric(df["Price Each"], errors="coerce")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df = df.dropna(subset=["Quantity Ordered", "Price Each", "Order Date"])

# 3. Feature Engineering
df["Month"] = df["Order Date"].dt.month
df["Sales"] = df["Quantity Ordered"] * df["Price Each"]
df["City"] = df["Purchase Address"].apply(lambda x: x.split(",")[1].strip())

print(f"Cleaned shape: {df.shape}")
print(f"Total Revenue: ₹{df['Sales'].sum():,.2f}")

# 4. Visualisations
plt.style.use("ggplot")

# Chart 1: Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()
plt.figure(figsize=(10, 5))
plt.bar(monthly_sales.index, monthly_sales.values / 1e5, color="#2b5c8f")
plt.xticks(range(1, 13))
plt.title("Monthly Sales Revenue (2025)")
plt.xlabel("Month")
plt.ylabel("Revenue (₹ Lakhs)")
plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=150)
plt.show()

# Chart 2: Sales by City
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
plt.bar(city_sales.index, city_sales.values / 1e5, color="#2e8b57")
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Revenue (₹ Lakhs)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("sales_by_city.png", dpi=150)
plt.show()

# Chart 3: Top-Selling Products
product_group = df.groupby("Product").agg(
    Total_Qty=("Quantity Ordered", "sum"),
    Total_Revenue=("Sales", "sum")
).sort_values("Total_Qty", ascending=True)

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.barh(product_group.index, product_group["Total_Qty"], color="#d97706")
ax1.set_title("Top-Selling Products by Quantity Sold")
ax1.set_xlabel("Units Sold")
plt.tight_layout()
plt.savefig("top_products.png", dpi=150)
plt.show()

# 5. Print Key Business Insights
best_month = monthly_sales.idxmax()
top_city = city_sales.idxmax()
top_rev_product = product_group["Total_Revenue"].idxmax()
top_qty_product = product_group["Total_Qty"].idxmax()

print("\n--- KEY BUSINESS INSIGHTS ---")
print(f"1. Peak Sales Month: Month {best_month} (₹{monthly_sales.max():,.2f})")
print(f"2. Top Performing City: {top_city} (₹{city_sales.max():,.2f})")
print(f"3. Most Sold Product (Volume): {top_qty_product} ({int(product_group.loc[top_qty_product, 'Total_Qty'])} units)")
print(f"4. Highest Revenue Product: {top_rev_product} (₹{product_group.loc[top_rev_product, 'Total_Revenue']:,.2f})")