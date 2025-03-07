import pandas as pd
import numpy as np
import yfinance as yf
from  datetime import datetime, timedelta

if __name__ == '__main__':
    stocks = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "ADBE", "CRM", "INTC",
        "AMD", "CSCO", "ORCL", "IBM", "QCOM", "JPM", "BAC", "WFC", "C", "GS", "MS", "BLK",
        "AXP", "V", "MA", "SCHW", "PNC", "USB", "SPGI", "TFC", "JNJ", "PFE", "MRK", "ABBV",
        "ABT", "LLY", "TMO", "DHR", "UNH", "BMY", "AMGN", "GILD", "MDT", "ISRG", "CVS",
        "PG", "KO", "PEP", "WMT", "COST", "NKE", "MCD", "SBUX", "HD", "LOW", "TGT", "DIS",
        "NFLX", "CMCSA", "T", "XOM", "CVX", "COP", "EOG", "SLB", "OXY", "PXD", "PSX", "VLO",
        "MPC", "KMI", "WMB", "HAL", "BKR", "DVN", "GE", "HON", "UNP", "UPS", "CAT", "DE",
        "LMT", "RTX", "BA", "MMM", "GD", "FDX", "EMR", "ETN", "NSC", "AMT", "PLD", "CCI",
        "EQIX", "PSA", "O", "DLR", "SPG", "WELL", "AVB", "EQR", "VTR", "BXP", "ARE", "INVH"
    ]
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=30)
    stock_data = yf.download(stocks, start=start_date, end=end_date)

    final_data = []
    for d in stock_data.index.unique("Date"):
        df = stock_data.loc[d]
        for stock in stocks:
            price = float(df.loc[('Close', stock)])

            # # Calculate daily returns and historical volatility
            change = stock_data[('Close', stock)].pct_change()
            historical_volatility = float(change.std() * np.sqrt(252))  #

            final_data.append({
                'date':d.date(),
                'stock':stock,
                'price': price,
                'volatility':historical_volatility,
            })

    df = pd.DataFrame(final_data)

    print("hi")
