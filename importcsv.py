import csv

with open("file1.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")

    dates = []
    prices = []

    for row in readCSV:
        date = row[0]
        price = row[1]

        dates.append(date)
        prices.append(price)

    print(dates)
    #print(prices)
