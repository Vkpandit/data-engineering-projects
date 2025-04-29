import pandas as pd
import pyodbc

df = pd.read_csv("sales_data_sample.csv")
df.dropna(inplace=True)
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=YourServer;DATABASE=YourDB;Trusted_Connection=yes;')
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""INSERT INTO Sales (Product, Quantity, SaleDate) VALUES (?, ?, ?)""", row.Product, row.Quantity, row.SaleDate)

conn.commit()
