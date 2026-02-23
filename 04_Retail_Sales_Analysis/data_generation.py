import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Realistic Data Generation for Portfolio
np.random.seed(42)
num_rows = 100000

data = {
    'Transaction_ID': range(1, num_rows + 1),
    'Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_rows)],
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Home Decor', 'Groceries', 'Books'], size=num_rows),
    'Quantity': np.random.randint(1, 10, size=num_rows),
    'Unit_Price': np.random.uniform(10, 1000, size=num_rows).round(2),
    'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], size=num_rows),
    'Payment_Method': np.random.choice(['Credit Card', 'UPI', 'Cash', 'Net Banking'], size=num_rows)
}

df = pd.DataFrame(data)
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
df['Profit'] = (df['Total_Sales'] * np.random.uniform(0.05, 0.25, size=num_rows)).round(2)

# Save the dataset
df.to_csv('retail_sales_100k.csv', index=False)
print("100,000 Rows Dataset Created Successfully!")
