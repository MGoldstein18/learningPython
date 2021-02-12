from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data.head())

month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses

plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')

plt.show()

plt.clf()

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')

plt.show()

expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

expense_categories = expense_overview.Expense
proportions = expense_overview.Proportion

plt.clf()

plt.pie(proportions, labels=expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

employees = pd.read_csv('employees.csv')
print(employees.head())

sorted_by_productivity = employees.sort_values(by=['Productivity'])
print(sorted_by_productivity)

employees_cut = sorted_by_productivity.head(100)

commute_times = sorted_by_productivity['Commute Time']
commute_times_log = np.log(commute_times)

print(commute_times.describe())

plt.clf()

plt.hist(commute_times_log)
plt.show()
