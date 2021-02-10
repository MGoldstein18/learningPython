import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# import all files and combine them into one dataframe
all_files = glob.glob('states*.csv')
data_list = []
for each_file in all_files:
    data = pd.read_csv(each_file)
    data_list.append(data)

us_census = pd.concat(data_list)

# change the income column from a object with a dollar sign to a numeric value we can use
us_census.Income = us_census.Income.replace('[\$,]', '', regex=True)

us_census.Income = pd.to_numeric(us_census.Income)

# change the GenderPop column into a two columns on numeric values we can use
gender_split = us_census.GenderPop.str.split('_')
us_census['Men'] = gender_split.str.get(0)
us_census['Women'] = gender_split.str.get(1)

# change the dataframe to get rid of unused columns
us_census = us_census[['State', 'TotalPop', 'Hispanic', 'White',
                       'Black', 'Native', 'Asian', 'Pacific', 'Income', 'Men', 'Women']]


us_census.Men = pd.to_numeric(us_census.Men.str[0:-1])
us_census.Women = pd.to_numeric(us_census.Women.str[0:-1])

# remove duplicate values from dataframe
us_census = us_census.drop_duplicates()

# fill in empty values in Women column
us_census = us_census.fillna(
    value={'Women': us_census.TotalPop - us_census.Men})

# create a scatter plot
plt.scatter(us_census.Women, us_census.Income)
plt.show()
