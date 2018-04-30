import numpy as np

my_data1 = [1, 2, 3, 4, 5, 6]
my_data2 = [7, 8, 9, 10, 11, 12]

my_array = np.column_stack((my_data1, my_data2))
my_array2 = np.row_stack((my_data1, my_data2))

print(my_array)

a = my_array[:, 0]
print(a)

b = my_array[0, :]
print(b)
