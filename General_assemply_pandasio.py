import pandas as pd

df = pd.read_csv('ZILLOW-Z77006_MLP3B.csv')

df = df.set_index('Date')

print(df.head())

df.to_csv('changedcsv.csv')

df2 = pd.read_csv('changedcsv.csv', index_col=0)

df2.columns = ['Austin HPI']

print(df2)
