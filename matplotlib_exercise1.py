import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [5, -2, 3, 4, 6, 9, 1]

plt.scatter(x, y, color='red')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Graph')
plt.xlim(-10, 20)
plt.ylim(-20, 20)

plt.show()
