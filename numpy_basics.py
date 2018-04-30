import numpy as np


def populate_array(list_name, col):
    a = 0

    for number in list_name:
        my_array[a, col] = number
        a += 1


prices_1 = [1000, 1100, 1200, 1300]
prices_2 = [2000, 2100, 2200, 2300]

my_array = np.zeros([len(prices_1), 2], dtype=float)

populate_array(prices_1, 0)
populate_array(prices_2, 1)

print(my_array)

print(my_array.shape)
print(my_array.ndim)
