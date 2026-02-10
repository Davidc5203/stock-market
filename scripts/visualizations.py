import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import sqlite3

connection = sqlite3.connect('data/stock_data.db')

'''
query = 
SELECT Ticker, AVG(Daily_Returns) AS Average_Returns
FROM stocks
WHERE Daily_Returns is NOT NULL
GROUP BY Ticker
ORDER BY Average_Returns DESC


average_returns = pd.read_sql_query(query, connection)

plt.bar( average_returns["Ticker"], average_returns["Average_Returns"] )
plt.xlabel("Ticker")
plt.ylabel("Average Returns")
plt.show()

'''


query_1 = '''

SELECT 

    Date, 
    Close,
    MA_50,
    MA_200

FROM stocks
WHERE Ticker = 'NVDA'
ORDER BY Date;

'''

price_moving = pd.read_sql_query(query_1, connection)

price_moving["Date"] = pd.to_datetime(price_moving["Date"], utc=True)

plt.plot(price_moving["Date"], price_moving["Close"], label = "Close Price")
plt.plot(price_moving["Date"], price_moving["MA_50"], label = "MA_50")
plt.plot(price_moving["Date"], price_moving["MA_200"], label = "MA_200")

plt.xlabel("Date")
plt.ylabel("Prices")
plt.legend()
plt.show()

















