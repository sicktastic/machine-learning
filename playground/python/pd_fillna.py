import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0], 
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                   columns=list('ABCD'))

print(df)
print("----------------")
print(df.fillna(method='ffill'))
