import os
import numpy as np
import pandas as pd

os.makedirs("sales_data", exist_ok=True)
np.random.seed(42)

products = {
    "USB-C Charging Cable": 499,
    "Wireless Earbuds": 1999,
    "Laptop Stand": 1299,
    "Mechanical Keyboard": 3499,
    "27in 4K Monitor": 24999,
    "Gaming Mouse": 1499,
    "Power Bank 20000mAh": 1799,
}
cities = [
    "Bengaluru, KA", "Mumbai, MH", "Delhi, DL",
    "Hyderabad, TS", "Pune, MH", "Chennai, TN"
]

for month in range(1, 13):
    n_rows = np.random.randint(300, 600)
    if month in [10, 11]:  # Festive season boost
        n_rows += 250

    chosen_products = np.random.choice(list(products.keys()), size=n_rows)
    dates = pd.date_range(f"2025-{month:02d}-01", periods=28, freq="D")

    df = pd.DataFrame({
        "Order ID": np.arange(10000 + month * 1000, 10000 + month * 1000 + n_rows),
        "Product": chosen_products,
        "Quantity Ordered": np.random.choice([1, 1, 1, 2, 3], size=n_rows),
        "Price Each": [products[p] for p in chosen_products],
        "Order Date": np.random.choice(dates, size=n_rows).astype(str),
        "Purchase Address": [f"{np.random.randint(10, 999)} Main Rd, {c}" for c in np.random.choice(cities, size=n_rows)]
    })

    # Add a few missing values to demonstrate data cleaning
    df.loc[df.sample(frac=0.02).index, "Quantity Ordered"] = np.nan
    df.to_csv(f"sales_data/sales_2025_{month:02d}.csv", index=False)

print("12 monthly CSV files created in 'sales_data/'.")