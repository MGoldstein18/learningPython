# import relevent Python modules
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

# load data
breast_cancer_data = load_breast_cancer()

# explore data
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

# split data for training and testing model
training_data, testing_data, training_labels, testing_labels = train_test_split(
    breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)

# create list and loop to hold and create the accuracies of the model using different k values
accuracies = []
for i in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors=i)
    classifier.fit(training_data, training_labels)
    print(i, classifier.score(testing_data, testing_labels))
    accuracies.append(classifier.score(testing_data, testing_labels))

# create a list of values for use as the x-axis/k values on our graph
k_list = range(1, 101)

# plot the accuracies of the different k values when used in the model
plt.plot(k_list, accuracies)
plt.xlabel('k value')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()
