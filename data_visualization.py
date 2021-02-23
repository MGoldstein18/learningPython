from matplotlib import pyplot as plt


# Visualization 1

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


# Visualization 2

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



# Visualization 3

from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]


plt.figure(figsize = (10, 8))
plt.bar(range(len(years)), past_years_averages, yerr = error, capsize = 5)
plt.axis([-0.5, 6.5, 70, 95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test Average')
plt.savefig('my_bar_chart.png')

plt.show()




# Visualization 4
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)\

middle_x = [(a + b) / 2 for a, b in zip(school_a_x, school_b_x)]

plt.figure(figsize = (10, 8))

ax = plt.subplot()

plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.legend(['Middle School A', 'Middle School B'])

plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

plt.savefig('my_side_by_side.png')

plt.show()