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
