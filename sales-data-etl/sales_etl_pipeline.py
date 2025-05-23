import pandas as pd
import pyodbc

df = pd.read_csv("C:/Users/VIKAS KUMAR PANDIT S/Documents/GitHub/data-engineering-projects/sales-data-etl/sales_data_sample.csv")
df.dropna(inplace=True)
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=PANDITS-LAPTOP\SQLEXPRESS;DATABASE=SQLProject;Trusted_Connection=yes;')
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1 FROM Sales WHERE Product = ? AND Quantity = ? AND SaleDate = ?
        )
        INSERT INTO Sales (Product, Quantity, SaleDate) VALUES (?, ?, ?)
    """, row.Product, row.Quantity, row.SaleDate, row.Product, row.Quantity, row.SaleDate)

conn.commit()
