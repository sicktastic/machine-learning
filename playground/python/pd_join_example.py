''' Build a dataframe in pandas'''
import pandas as pd

def test_run():
    csv_file = "../../datasets/stock/SPY.csv"

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

    # Join the two dtaframes using DataFrame.join()
    df1 = df1.join(dfSPY)

    # Drop NaN Values
    df1 = df1.dropna()

    print(df1)


if __name__ == "__main__":
    test_run()
