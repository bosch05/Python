import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def manual_data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145,'2016 - 01 - 01','Bosch',5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M: %S'))
    keyword = 'Python'
    value = random.randrange(0, 1000)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value))
    conn.commit()


def read_from_db():


create_table()

for i in range(1000):
    dynamic_data_entry()

c.close()
conn.close()
