import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

# loop through each column in the dataframe and create a bar chart for it
for each in columns:
    sns.countplot(df[each], order=df[each].value_counts().index)
    plt.xticks(rotation=30, fontsize=10)
    plt.xlabel(each, fontsize=12)
    plt.title(each + ' Value Counts')
    plt.show()
    plt.clf()
