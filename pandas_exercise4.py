import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data from csv file
# check column names
# set index
# check data types

df = pd.read_csv('topix.csv', index_col='Ticker')
print(df.shape)

print(list(df))

df.columns = [
    'Name',
    'OPM',
    'Mcap',
    'DivY',
    'ICB_subsector',
    'ICB_supersector',
    'PBR',
    'PER'
]

print(df.count())
df = df.dropna()
print('\n', df.count())
