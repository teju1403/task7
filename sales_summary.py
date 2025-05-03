import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite DB
conn = sqlite3.connect("sales_data.db")

# SQL Query: Group by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Load result into DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Print result
print("Sales Summary:")
print(df)

# Plot bar chart of revenue
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product', legend=False)
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
