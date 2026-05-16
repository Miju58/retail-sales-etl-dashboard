import pandas as pd
import mysql.connector

# Load cleaned data
sales = pd.read_csv("./data/Superstore.csv", encoding="latin1")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2002",
    database="retail_etl"
)

cursor = conn.cursor()

# Insert data
for _, row in sales.iterrows():

    sql = """
    INSERT INTO sales
    (Order_ID, Product_Name, Quantity, Sales, Profit)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        row["Order ID"],
        row["Product Name"],
        row["Quantity"],
        row["Sales"],
        row["Profit"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Data loaded successfully!")

cursor.close()
conn.close()