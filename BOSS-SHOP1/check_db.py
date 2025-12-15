import sqlite3
import os

# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'frontend', 'database.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"- {table[0]}")

# Get categories
print("\nCategories:")
cursor.execute("SELECT DISTINCT category FROM products;")
categories = cursor.fetchall()
for category in categories:
    print(f"- {category[0]}")

# Get product count by category
print("\nProduct count by category:")
for category in categories:
    cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?;", (category[0],))
    count = cursor.fetchone()[0]
    print(f"- {category[0]}: {count} products")

conn.close()