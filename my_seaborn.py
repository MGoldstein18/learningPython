from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# load match stats into dataframe
df = pd.read_csv('WorldCupMatches.csv')

# add total goal column to dataframe and display first few rows
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

# create bar chart using Seaborn to visualize goals per world cup
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1.25)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(
    data=df,
    x='Year',
    y='Total Goals'
)
ax.set_title('Goals per World Cup')

plt.show()

# load the goals csv into a dataframe
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

# create a box plot for the goals per world cup
f, ax2 = plt.subplots(figsize=(12, 7))
ax2.set_title('Box Plot of Goals at each World Cup')
ax2 = sns.boxplot(
    data=df_goals,
    x='year',
    y='goals'
)

plt.show()
