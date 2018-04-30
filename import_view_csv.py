import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import datetime as dt

filename = 'file1.csv'
dates = []
prices = []

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")

    for row in readCSV:
        date = row[0]
        price = row[1]
        dates.append(date)
        prices.append(float(price))

dates = [dt.datetime.strptime(d, '%d/%m/%Y').date() for d in dates]

style.use("ggplot")

plt.plot(dates, prices, linewidth=2)
plt.title("Bosch Chart")
plt.ylabel("Price")
plt.xlabel("Date")

plt.legend()
plt.show()
