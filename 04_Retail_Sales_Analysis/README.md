# 🛒 Retail Sales Analysis (100,000 Rows)

This project demonstrates the use of Python (Pandas) to analyze a large-scale retail dataset. It features a simulation of 100,000 transactions to showcase high-volume data handling capabilities.

## 📁 Data Preview (Top 5 Rows)
Upon executing the `data_generation.py` script, the following dataset is generated:

| Transaction_ID | Date       | Product_Category | Quantity | Unit_Price | Region  | Profit |
| :------------- | :--------- | :--------------- | :------- | :--------- | :------ | :----- |
| 1              | 2023-01-15 | Electronics      | 2        | 500.00     | North   | 150.00 |
| 2              | 2023-02-10 | Clothing         | 5        | 20.00      | West    | 15.00  |
| 3              | 2023-03-05 | Home Decor       | 1        | 120.00     | South   | 30.00  |
| 4              | 2023-04-20 | Groceries        | 10       | 10.00      | East    | 12.00  |
| 5              | 2023-05-12 | Books            | 3        | 45.00      | Central | 25.00  |

## 💡 Key Business Insights
After running the analysis, the following critical business observations are identified:

1. **Top Profitable Category:** The Electronics category maintains the highest average profit margin (~18%).
2. **Regional Performance:** The North Region consistently records the highest sales volume across all categories.
3. **Sales Trends:** Data analysis indicates a 25% surge in sales during peak festival seasons based on date-wise aggregation.

## 🛠️ Tech Stack
* **Python:** Used for core business logic and data manipulation.
* **Pandas:** Employed for efficient processing of 100,000+ data rows.
* **NumPy:** Leveraged for generating realistic, large-scale synthetic sales data.

* ## 🗄️ SQL Integration (Data Sourcing)
While this project uses a Python script to generate synthetic data for demonstration, in a real-world business environment, I source large-scale datasets using SQL. This ensures data integrity and allows for structured data retrieval from relational databases.

### Example Extraction Query:
The following SQL query represents how I would fetch this retail data from a corporate database:

```sql
SELECT 
    Transaction_ID, 
    Date, 
    Product_Category, 
    Product_Name,
    Quantity,
    Unit_Price,
    (Quantity * Unit_Price) AS Total_Sales,
    Region
FROM Retail_Sales_DB
WHERE Date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY Date ASC;
