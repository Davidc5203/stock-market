import sqlite3
import pandas as pd

connection = sqlite3.connect('data/stock_data.db')

#finding the top 5 average returns
query = '''
SELECT Ticker, AVG(Daily_Returns) AS Average_Returns
FROM stocks
WHERE Daily_Returns is NOT NULL
GROUP BY 1
ORDER BY Average_Returns DESC
LIMIT 5;
'''

average_returns = pd.read_sql_query(query, connection)
#print(average_returns)

#finding which stocks has the highest average volatility

query_1 = '''

SELECT Ticker, AVG(Volatility) AS Average_Volatility
FROM stocks
WHERE Volatility is NOT NULL
GROUP BY 1 
ORDER BY Average_Volatility DESC
LIMIT 5;
'''

average_volatility = pd.read_sql_query(query_1, connection)
#print("These are the 5 highest average volatility:\n",average_volatility)

#Best performing stock overall

query_2 = '''

SELECT

    a.Ticker,
    a1.Close AS First_Price,
    a2.Close AS Last_Price,
    (a2.Close - a1.Close) / a1.Close AS Total_Return

FROM stocks AS a 
JOIN stocks AS a1
  ON a.Ticker = a1.Ticker
   AND a1.Date = (SELECT MIN(DATE) 
                  FROM stocks
                  WHERE Ticker = a.Ticker)
JOIN stocks AS a2
  ON a.Ticker = a2.Ticker 
   AND a2.Date = (SELECT MAX(DATE)
                  FROM stocks
                  WHERE Ticker = a.Ticker)
GROUP BY a.Ticker
ORDER BY Total_Return DESC

'''

top_performance = pd.read_sql_query(query_2, connection)
#print(top_performance)

#Best single trading day

query_3 = '''

SELECT Ticker, Date, Daily_Returns
FROM stocks
ORDER BY Daily_Returns DESC
LIMIT 5;

'''

best_trading_day = pd.read_sql_query(query_3, connection)
#print(best_trading_day)


#Risk and Return Tradeoff

query_4 = '''

SELECT 

    Ticker,
    AVG(Daily_Returns) AS Average_Returns,
    AVG(Volatility) AS Average_Volatility

FROM stocks
GROUP BY Ticker
ORDER BY Average_Returns DESC;

'''

risk_return = pd.read_sql_query(query_4, connection)
print(risk_return)

