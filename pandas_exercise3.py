import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import data from csv file (no headers in file)
df = pd.read_csv('topix.csv', index_col='Ticker')

df.columns = ['Name', 'OPM', 'Mcap', 'DivY', 'ICB_subsector', 'ICB_supersector', 'PBR', 'PER']


df = df.sort_values('PBR')
df = df.head(1000)

df = df.dropna()
print(df.count())

plt.bar(df['PBR'], df['OPM'], label='scatter', color='orange')
plt.xlabel('OPM')
plt.ylabel('PBR')
plt.legend()
plt.title('Bosch')
plt.show()
