import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table (SQL inside triple quotes)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""") 

# Sample data to insert
sales_data = [
    ('Apples', 10, 2.5),
    ('Oranges', 5, 3.0),
    ('Bananas', 8, 1.8),
    ('Apples', 7, 2.5),
    ('Oranges', 10, 3.0),
    ('Bananas', 12, 1.8),
]

# Insert the data
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

# Save and close
conn.commit()
conn.close()

print("Database created and sample data inserted successfully.")
