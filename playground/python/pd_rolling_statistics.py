""" Utility functions """

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="../../datasets/stock/"):
    """ Returns CSV file path given ticker symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files. """
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),
                         index_col = 'Date', 
                         parse_dates = True, 
                         usecols = ['Date', 'Adj Close'], 
                         na_values = ['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        # df = df.join(df_temp, how = "inner")
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset = ['SPY'])

    return df

def plot_data(df, title="Stock prices"):
    ''' Plot stock prices '''
    ax = df.plot(title = title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    # Compute rolling mean using a 20-day window
    rm_SPY = pd.Series.rolling(df['SPY'], window=20).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    plot_data(rm_SPY)

if __name__ == "__main__":
    test_run()
