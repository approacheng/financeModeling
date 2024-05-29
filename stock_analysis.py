import yfinance as yf
import pandas as pd

# Define the stock symbols for the companies
stocks = {
    "Amazon": "AMZN",
    "Google": "GOOGL",
    "Tesla": "TSLA",
    "Apple": "AAPL",
    "Boeing": "BA"
}

# Define the period for the last quarter (approximately 3 months)
period = "3mo"

# Download stock data for the last quarter
data = {name: yf.Ticker(symbol).history(period=period) for name, symbol in stocks.items()}

# Extract the closing prices for the period
closing_prices = {name: df['Close'] for name, df in data.items()}

# Create a DataFrame for the closing prices
df_closing = pd.DataFrame(closing_prices)

# Calculate the percentage change over the last quarter
performance = df_closing.pct_change().dropna().add(1).cumprod().iloc[-1].sub(1).mul(100)

print(performance)
