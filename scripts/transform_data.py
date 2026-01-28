import pandas as pd

stocks = pd.read_csv("data/stock_data.csv")

def calculate_returns(df):

    df['Daily_Returns'] = df.groupby("Ticker")["Close"].pct_change()

    return df

stocks = calculate_returns(stocks)

#print(stocks.groupby("Ticker")[['Ticker', 'Close', 'Daily_Returns']].head(3))

def calculate_moving_averages(df):

    df['MA_50'] = df.groupby('Ticker')['Close'].rolling(window=50).mean().reset_index(level=0, drop=True)

    df['MA_200'] = df.groupby('Ticker')['Close'].rolling(window=200).mean().reset_index(level=0, drop=True)


    return df

stocks = calculate_moving_averages(stocks)
#print(stocks[['Ticker', 'Close', 'MA_50', 'MA_200']].head(60))


def calculate_volatility(df):

    df["Volatility"] = df.groupby("Ticker")["Daily_Returns"].rolling(window=30).std().reset_index(level=0, drop=True)

    return df

stocks = calculate_volatility(stocks)
print(stocks[["Ticker", "Daily_Returns", "Volatility"]].tail(20))

stocks.to_csv("data/transformed_stock_data.csv", index = False)