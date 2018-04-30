import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import data from csv file (no headers in file)
df = pd.read_csv('topix.csv', index_col='Ticker')

# PRINT SHAPE OF DATAFRAME
print(df.shape)

# PRINT COLUMN NAMES
print(list(df))

df.columns = ['Name', 'OPM', 'Mcap', 'DivY', 'ICB_subsector', 'ICB_supersector', 'PBR', 'PER']

# PRINT DATA TYPES
print(df.dtypes)

print(df.count())
df = df.dropna()
print(df.count())

# PRINT COLUMN NAMES
print(list(df))

print(df.describe())

plt.plot()
