import pandas as pd
import matplotlib.pyplot as plt

# import data from csv file (no headers in file)
df = pd.read_csv('Toyota.csv', usecols=[0, 1, 2], header=None, names=['Date', 'Mcap', 'Profit'], index_col='Date')

# look to see what file looks like
print(df.head())

print(df.describe())

multiple = df['Mcap'] / df['Profit']

print(multiple.describe())
df.Mcap.plot()
df.Profit.plot(secondary_y=True,style='g')
plt.show()
