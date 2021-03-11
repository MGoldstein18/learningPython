# import relevent modules

import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

# function which takes a dataframe of a player's data and analyses it


def strike_zone(dataframe):
    fig, ax = plt.subplots()

    # change value of type of pitch to 1 and 0 so that it can be used as labels for our model
    dataframe.type = dataframe.type.map({'S': 1, 'B': 0})

    # drop NaN values from the columns we need
    dataframe = dataframe.dropna(subset=['plate_x', 'plate_z', 'type'])

    # create scatter plot of location of pitches and colored according to type
    plt.scatter(x=dataframe.plate_x, y=dataframe.plate_z,
                c=dataframe.type, cmap=plt.cm.coolwarm, alpha=0.25)
    plt.title(dataframe['player_name'][4] + ' Strike Zone')

    # split data into training and validation sets
    training_set, validation_set = train_test_split(dataframe, random_state=1)

    # create model
    classifier = SVC(kernel='rbf', gamma=0.5, C=1)
    # train model
    classifier.fit(training_set[['plate_x', 'plate_z']], training_set.type)
    # draw boundary onto graph
    draw_boundary(ax, classifier)

    # print the score of the model
    print(classifier.score(
        validation_set[['plate_x', 'plate_z']], validation_set.type))

    # ensure same axis and display graphs
    ax.set_ylim(-2, 6)
    ax.set_xlim(-3, 3)
    plt.show()


# call function on the players
strike_zone(aaron_judge)
strike_zone(jose_altuve)
strike_zone(david_ortiz)
