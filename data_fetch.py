import yfinance as yf
import pandas as pd

def fetch_data():
    stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

    data = pd.DataFrame()

    for stock in stocks:
        df = yf.download(stock, start="2020-01-01", end="2023-01-01")
        data[stock] = df['Close']

    data.dropna(inplace=True)
    data.to_csv("stock_data.csv")

    print("Data saved as stock_data.csv")

if __name__ == "__main__":
    fetch_data()