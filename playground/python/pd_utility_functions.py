""" Utility functions """

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="../../datasets/stock/"):
    """ Returns CSV file path given ticker symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files. """
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:

    return df
