''' Build a dataframe in pandas'''
import pandas as pd

def test_run():
    csv_path = "../../datasets/stock/"
    csv_file = csv_path +  "SPY.csv"

    # Define data range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    df1 = pd.DataFrame(index = dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv(csv_file, index_col = "Date", 
            parse_dates = True, usecols = ['Date', 'Adj Close'],
            na_values = ['nan'])

    # Rename 'Adj Close' colum to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns = {'Adj Close': 'SPY'})

    # Join the two dtaframes using DataFrame.join()
    df1 = df1.join(dfSPY, how = "inner")

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv(csv_path + "{}.csv".format(symbol),
                              index_col = 'Date',
                              parse_dates = True,
                              usecols = ['Date', 'Adj Close'],
                              na_values = ['nan'])

        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df1 = df1.join(df_temp)

    print(df1)

if __name__ == "__main__":
    test_run()
