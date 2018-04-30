import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

file_name = 'data.csv'

price_array = np.loadtxt(file_name, delimiter=',', usecols=[1])

eps_array = np.loadtxt(file_name, delimiter=',', usecols=[2])

per_array = price_array / eps_array

print(np.mean(per_array))
print(np.median(per_array))
print(np.corrcoef(price_array, eps_array))

style.use("ggplot")

plt.plot(per_array, linewidth=3, label="Line one")
plt.title("Bosch Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.legend()
plt.show()
