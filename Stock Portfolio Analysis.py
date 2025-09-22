"""
Task List

1. Data Collection and String Formatting:
   - Create a list of five stock ticker symbols.
   - Use a for loop to fetch each company's longName with yfinance.
   - Print formatted strings: "The company name for <tic> is <co_name>".

2. Historical Data Retrieval:
   - For each stock, fetch 5 years of historical data.
   - Print the last 3 rows to confirm data was retrieved correctly.
   - Store closing prices for all stocks in a DataFrame (prc_df).

3. Advanced Data Handling and Analysis:
   - Calculate daily returns for each stock (ret_df).
   - Identify the date and value of the maximum daily return for each stock.

4. Portfolio Analysis:
   - Assume an initial investment of $10,000, equally distributed ($2000 each).
   - Use cumulative returns to calculate the portfolio's growth.
   - Print the portfolio value at the end of the 5 years.

"""

# Importing libraries
import yfinance as yf
import pandas as pd

# ===Task 1: Data Collection and String Formatting===
# Creating a list of five ticker symbols and printing their full company names

ticker = ("AAPL", "GOOG", "AMZN", "TSLA", "MSFT")
stock = yf.Ticker # defining the Ticker class for easier use

for tic in ticker:
    co_name = stock(tic).info["longName"] # fetching the long name of each company
    
    print(f"The company name for {tic} is {co_name}")
print()

# ===Task 2 & 3: Historical Data Retrieval and===
# ===Advanced Data Handling and Analysis===

prc_df = pd.DataFrame()
ret_df = pd.DataFrame()
for tic in ticker:
    hist_prc = stock(tic).history("5y")  # fetch 5 years of historical prices
    prc_df[tic] = hist_prc["Close"]          # store only the Close column in prc_df
    
    print(f"5-Year Historical Price of {tic}")
    print(hist_prc.tail(3)) # print last 3 rows from the historical price dataframe
    print()

print("Closing price of each stock")
print(prc_df)
print()

# Calculating daily returns for each stock

print("Daily Return of each stock")

ret_df = prc_df.pct_change()    # compute daily percentage change

print(ret_df)
print()

# Identify the maximum daily return for each stock along with the date

for tic in ticker:
    max_date = ret_df[tic].idxmax()  # fetching the date based on the max return
    
    print(f"Max return for {tic} is on {max_date}, return is {ret_df.loc[max_date,tic]:.2%}")
print()

# ===Task 4: Portfolio Analysis===
# Calculate cumulative returns 
 
cuml_ret = (1 + ret_df).cumprod()

print("Cumulative return of each stock")
print(cuml_ret)
print()

INV = 10000                 # the total initial investment
weight = INV / len(ticker)  # equal allocation per stock ($2000 each)

per_stock_value = weight * cuml_ret                 # value of each $2000 stock investment over time
port_value = per_stock_value.sum(axis=1).iloc[-1]   # total portfolio value at the end

print(f"Portfolio initial value is ${INV}")
print(f"Portfolio value at the end of the 5 years is ${port_value:.2f}")