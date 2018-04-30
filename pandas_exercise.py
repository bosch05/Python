import numpy as np
import pandas as pd

my_array = np.array([
    [1605, 12, 1.0, 2.0],
    [6301, 20, 2.5, 1.2],
    [7203, 15, 1.0, 2.0],
    [4508, 20, 2, 0.50],
    [6135, 25, 4, 0.25]
])

my_array2 = np.array([
    [1606, 15, 1.0, 2.0],
    [6302, 16, 1.2, 1.8],
    [7204, 17, 1.4, 1.6],
    [4503, 18, 1.6, 1.4],
    [6144, 19, 2.0, 1.2]
])

# SET NAMES TO COLUMNS
df = pd.DataFrame(my_array, columns=['TICKER', 'PER', 'PBR', 'DIV_YIELD'])

# SET INDEX COLUMN
df = df.set_index('TICKER')

# SET NAMES TO COLUMNS
df1 = pd.DataFrame(my_array2, columns=['TICKER', 'PER', 'PBR', 'DIV_YIELD'])

# SET INDEX COLUMN
df1 = df1.set_index('TICKER')

# SELECTING COLUMNS BY LABEL
df_per = df[['PER']]

# SELECTING ROWS BY INDEX
df_1605 = df.iloc[0]

# SELECTING ROWS BY INDEX
df_1605 = df.loc[1605]

# EXTRACTING USING BOOLEAN CONDITIONS
df_boolean = df['PER'] < 15

# SORTING DATA - SAME DATAFRAME
df.sort_values(by='PER', inplace=True)

# SPLITTING DATAFRAMES BY ROWS
new_df1 = df.iloc[0:2]
new_df2 = df.iloc[2:4]

# ADDING NEW COLUMN WITH DATA
df['FCF YIELD'] = [7, 6, 5, 4, 3]

# COMBINING DATAFRAMES

df2 = df.append(df1)

# SORTING DATA - SAME DATAFRAME
df2.sort_values(by='PER', inplace=True)

print(df2.dtypes)
