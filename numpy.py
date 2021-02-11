# Task 1


import pandas as pd
import numpy as np
from weather_data import london_data

# examine the data by printing the first 5 rows
print(london_data.head())

# get and display the average temp, variance and standard variation
temp = london_data.TemperatureC
average_temp = np.average(temp)
temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)

print(average_temp, temperature_var, temperature_standard_deviation)

# drill down on June and July by getting all their data and using it for the mean and standard variation
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

june_mean = np.average(june)
july_mean = np.average(july)

june_std = np.std(june)
july_std = np.std(july)

print(june_mean, june_std, july_mean, july_std)

# a dictionary of all the months
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'Sepetember', 10: 'October', 11: 'November', 12: 'December'}

# loop through each month and display the average temp and standard deviation in an appropriate sentence
for i in range(1, 13):
    month = london_data.loc[london_data["month"] == i]["TemperatureC"]
    print("The mean temperature in " +
          months[i] + " is " + str(np.mean(month)))
    print("The standard deviation of temperature in " +
          months[i] + " is " + str(np.std(month)) + "\n")


# Task 2
mport pandas as pd

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

print(car_eval.manufacturer_country.value_counts())
print(car_eval.manufacturer_country.value_counts(dropna=False, normalize=True))

print(car_eval.buying_cost.unique())

buying_cost_categories = ['low', 'med', 'high', 'vhigh']

car_eval.buying_cost = pd.Categorical(
    car_eval.buying_cost, buying_cost_categories, ordered=True)

print(buying_cost_categories[int(np.median(car_eval.buying_cost.cat.codes))])

print(car_eval.luggage.value_counts(dropna=False, normalize=True))
print(car_eval.luggage.value_counts(normalize=True))
print(car_eval.luggage.value_counts()/len(car_eval.luggage))

print((car_eval.doors == '5more').sum())
print((car_eval.doors == '5more').mean())
