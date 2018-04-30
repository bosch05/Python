import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import data from csv file (no headers in file)
df = pd.read_csv('topix.csv', index_col='Ticker')

df.columns = ['Name', 'OPM', 'Mcap', 'DivY', 'ICB_subsector', 'ICB_supersector', 'PBR', 'PER']

df = df.dropna()

df = df.head(50)

fig = plt.figure()

graph1 = fig.add_subplot(2, 2, 1)
graph1.scatter(df['OPM'], df['PER'])

graph2 = fig.add_subplot(2, 2, 2)
graph2.scatter(df['OPM'], df['PBR'])


plt.show()
