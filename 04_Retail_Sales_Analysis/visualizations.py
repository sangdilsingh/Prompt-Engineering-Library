import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('retail_sales_100k.csv')

# 1. Sales Trend over Time
df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.resample('M', on='Date')['Total_Sales'].sum()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales)
plt.title('Monthly Sales Trend (100k Transactions)')
plt.ylabel('Total Sales ($)')
plt.savefig('sales_trend.png') # Graph save kar liya
print("Sales trend chart generated!")

# 2. Profit by Category (Seaborn Barplot)
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_Category', y='Profit', data=df, estimator=sum)
plt.title('Total Profit by Category')
plt.savefig('category_profit.png')
print("Profit chart generated!")
