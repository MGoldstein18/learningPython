from matplotlib import pyplot as plt

x = range(12)
y1 = range(124, 268, 12)
y2 = range(175, 475, 25)

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['y1', 'y2'], loc=4)
plt.show()
