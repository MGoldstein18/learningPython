import numpy as np
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


past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]


plt.figure(figsize=(10, 8))
plt.bar(range(len(years)), past_years_averages, yerr=error, capsize=5)
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

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]


school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)\

middle_x = [(a + b) / 2 for a, b in zip(school_a_x, school_b_x)]

plt.figure(figsize=(10, 8))

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


# Visualization 5

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

plt.figure(figsize=(10, 8))

plt.bar(range(len(unit_topics)), As)
plt.bar(range(len(unit_topics)), Bs, bottom=As)
plt.bar(range(len(unit_topics)), Cs, bottom=c_bottom)
plt.bar(range(len(unit_topics)), Ds, bottom=d_bottom)
plt.bar(range(len(unit_topics)), Fs, bottom=f_bottom)

ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

plt.legend(['A', 'B', 'C', 'D', 'F'])
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

plt.savefig('my_stacked_bar.png')

plt.show()


# Visualization 6


exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13,
                90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48, 78.81, 79.23, 74.38, 79.27, 81.07, 75.42, 90.35, 82.93, 86.74, 81.33,
                95.1, 86.57, 83.66, 85.58, 81.87, 92.14, 72.15, 91.64, 74.21, 89.04, 76.54, 81.9, 96.5, 80.05, 74.77, 72.26, 73.23, 92.6, 66.22, 70.09, 77.2]

plt.figure(figsize=(10, 8))

plt.hist(exam_scores1, bins=12, normed=True, histtype='step', linewidth=2)
plt.hist(exam_scores2, bins=12, normed=True, histtype='step', linewidth=2)

plt.legend(['1st Yr Teaching', '2nd Yr Teaching'])
plt.title('Final Exam Score Distribution')
plt.xlabel('Percentage')
plt.ylabel('Frequency')

plt.savefig('my_histogram.png')

plt.show()


# Visualization 7


unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

plt.figure(figsize=(10, 8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis('equal')

plt.title('Hardest Topics')

plt.savefig('my_pie_chart.png')

plt.show()


# Visualization 8


hours_reported = [3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75, 4,
                  4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85,
               74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

plt.figure(figsize=(10, 8))

hours_lower_bound = [i * 0.8 for i in hours_reported]
hours_upper_bound = [i * 1.2 for i in hours_reported]

plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)

plt.plot(exam_scores, hours_reported, linewidth=2)

plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')

plt.savefig('my_line_graph.png')

plt.show()
