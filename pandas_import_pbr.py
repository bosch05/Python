import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# import data from csv file
dftopix = pd.read_csv('topixPBR.csv')
df7203 = pd.read_csv('7203PBR.csv')

# parse dates, set index and sort by index
dftopix['Dates'] = pd.to_datetime(dftopix['Dates'], dayfirst=True)
dftopix = dftopix.set_index(['Dates'])
dftopix = dftopix.sort_index()

df7203['Dates'] = pd.to_datetime(df7203['Dates'], dayfirst=True)
df7203 = df7203.set_index(['Dates'])
df7203 = df7203.sort_index()

# merge two dataframes by index
dfmerged = pd.merge(dftopix, df7203, left_index=True, right_index=True)

# rename columns in new dataframe
dfmerged.columns = ['TopixPBR', 'ToyotaPBR']

# create new column
dfmerged['RELPBR'] = dfmerged['ToyotaPBR'] / dfmerged['TopixPBR']

# PRINT HEAD
print(dfmerged.head(10))

# PRINT TAIL
print(dfmerged.tail(10))

plt.plot(dfmerged['ToyotaPBR'])
plt.show()
