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


# Project 2

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495,
                    16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0,
                       79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0,
                           83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0,
                         74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12, 8))
x_values = range(len(months))

ax1 = plt.subplot(1, 2, 1)
plt.plot(x_values, visits_per_month, marker='o')
plt.xlabel('months')
plt.ylabel('visitors')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Number of Visitors to the Website per Month')

ax2 = plt.subplot(1, 2, 2)
plt.plot(x_values, key_limes_per_month, color='blue')
plt.plot(x_values, persian_limes_per_month, color='green')
plt.plot(x_values, blood_limes_per_month, color='red')
plt.legend(['Key Limes', 'Persian Limes', 'Blood Limes'])
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.xlabel('months')
plt.ylabel('Number of Limes Sold')
plt.title('Number of Limes Sold Each Month')

plt.savefig('visitors_and_limes_sold.png')

plt.show()
