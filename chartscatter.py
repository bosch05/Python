
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 11, 18, 24, 32, 44, 55, 70]


plt.scatter(x, y, label="Line one")
plt.title("Bosch Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
