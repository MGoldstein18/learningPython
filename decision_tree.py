# import relevent modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# load flag data
flags = pd.read_csv('flags.csv', header=0)

# get labels and data to classify flags
labels = flags.Landmass
data = flags[['Red', 'Green', 'Blue', 'Gold', 'White', 'Black', 'Orange',
              'Circles', 'Crosses', 'Saltires', 'Quarters', 'Sunstars', 'Crescent', 'Triangle']]

# split data for training and testing
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, random_state=1)

# create list to hold accuracy scores of models
scores = []

# loop through a range of decision tree models to test which depth provides the most accurate score
for i in range(1, 21):
    tree = DecisionTreeClassifier(random_state=1, max_depth=i)
    tree.fit(train_data, train_labels)
    scores.append(tree.score(test_data, test_labels))

# plot the scores on a graph
plt.plot(range(1, 21), scores)
plt.show()
