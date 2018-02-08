import pandas as pd
import matplotlib.pyplot as plt

def get_max_close(symbol):
    """
    Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: dataset/<symbol>.csv
    """
    df = pd.read_csv("../../datasets/{}.csv".format(symbol)) # read in data

    return df['Close'].max() # comput and return max

def test_run():
    # Function called by Test Run.
    for symbol in ['HCP']:
        print("Max close")
        print(symbol, get_max_close(symbol))

if __name__ == "__main__":
    test_run()
