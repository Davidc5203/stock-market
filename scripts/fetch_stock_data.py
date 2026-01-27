import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

tickers = ["NVDA", "INTC", "GOOGL", "META", "MSFT"]

def fetch_stocks(ticker, start_date, end_date):

    tick = yf.Ticker(ticker)

    historical_data = tick.history(start = start_date, end= end_date)

    return historical_data

stock_list = []

for tick in tickers:

    data = fetch_stocks(tick, "2020-12-01", "2025-12-01")

    data["Ticker"] = tick

    stock_list.append(data)

all_stock_list = pd.concat(stock_list)

all_stock_list.to_csv("data/stock_data.csv")













