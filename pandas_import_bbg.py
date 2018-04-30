import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# import data from csv file
dfPER = pd.read_csv('7203PER.csv')
dfPBR = pd.read_csv('7203PBR.csv')

# parse dates, set index and sort by index
dfPER['Dates'] = pd.to_datetime(dfPER['Dates'], dayfirst=True)
dfPER = dfPER.set_index(['Dates'])
dfPER = dfPER.sort_index()

dfPBR['Dates'] = pd.to_datetime(dfPBR['Dates'], dayfirst=True)
dfPBR = dfPBR.set_index(['Dates'])
dfPBR = dfPBR.sort_index()

# merge two dataframes by index
dfmerged = pd.merge(dfPER, dfPBR, left_index=True, right_index=True)

# rename columns in new dataframe
dfmerged.columns = ['PER', 'PBR']

# PRINT HEAD
print(dfmerged.head(10))

# PRINT TAIL
print(dfmerged.tail(10))

#print(dfPER[datetime(2017, 1, 1):])

last5years = dfmerged[datetime(2012, 1, 1):]
print(last5years.describe())


plt.scatter(last5years['PER'], last5years['PBR'])
plt.show()
