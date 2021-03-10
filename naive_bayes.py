# import necessary Python modules
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# fetch emails from the 2 categories we want
emails = fetch_20newsgroups(
    categories=['rec.sport.baseball', 'rec.sport.hockey'])

# explore the data
print(emails.target_names)
print(emails.data[5])
print(emails.target[5])

# split the data into training and testing data
train_emails = fetch_20newsgroups(categories=[
                                  'comp.sys.ibm.pc.hardware', 'rec.sport.hockey'], subset='train', shuffle=True, random_state=108)

test_emails = fetch_20newsgroups(categories=[
                                 'rec.sport.baseball', 'rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

# initialize and use a CountVectorizer object to count each word
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# initialize and use a multinomialNB model to be trained and analyse data
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)
print(classifier.score(test_counts, test_emails.target))
