import sqlite3
import pandas as pd

df = pd.read_csv("data/transformed_stock_data.csv")

connection = sqlite3.connect("data/stock_data.db")

df.to_sql('stocks', connection, if_exists='replace', index=False)

connection.close()

