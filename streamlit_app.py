import yfinance as yf
import pandas as pd
import streamlit as st

# Define the ticker and risk-free rate
ticker = 'MSFT'
rf_monthly = 0.0025  # 0.25% per month

st.title("Microsoft (MSFT) Sharpe Ratio")

# Download monthly stock price data for the past 5 years
data = yf.download(ticker, period='5y', interval='1mo', auto_adjust=True)

if not data.empty:
    close_prices = data['Close'].squeeze()

    # Calculate monthly returns
    monthly_returns = close_prices.pct_change().dropna()

    # Calculate average excess return and standard deviation
    excess_returns = monthly_returns - rf_monthly
    mean_excess_return = excess_returns.mean()
    std_dev_return = monthly_returns.std()

    # Calculate the monthly Sharpe Ratio
    if std_dev_return > 0:
        monthly_sharpe_ratio = mean_excess_return / std_dev_return

        st.write(f"Ticker: {ticker}")
        st.metric(label="Monthly Sharpe Ratio", value=f"{monthly_sharpe_ratio:.3f}")
    else:
        st.error("Unable to calculate Sharpe Ratio.")
else:
    st.error("No data found for MSFT.")
  
