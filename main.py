import os
import numpy as np
import pickle
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

folder = 'email/'

files = os.listdir(folder)

emails = [folder + file for file in files]

words = []
for email in emails:
    f = open(email, encoding='latin-1')
    blob = f.read()
    words += blob.split(" ")
for i in range(len(words)):
    if not words[i].isalpha():
        words[i] = ""

word_dict = Counter(words)
len(word_dict)

del word_dict[""]

word_dict = word_dict.most_common(3000)

for i in word_dict:
    print(i)

features = []

labels = []

for email in emails:
    f = open(email, encoding='latin-1')
    blob = f.read().split(" ")
    data = []
    for i in word_dict:
        data.append(blob.count(i[0]))

    features.append(data)

    if 'spam' in email:
        labels.append(1)
    if 'ham' in email:
        labels.append(0)
features = np.array(features)

labels = np.array(labels)

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=9)

clf = MultinomialNB()

clf.fit(x_train, y_train)

mail = """


"""

input_mail =[]
for i in word_dict:
    input_mail.append(mail.count(i[0]))

clf.predict(np.array(input_mail).reshape(1, 3000))

y_pred = clf.predict(x_test)

accuracy_score(y_pred, y_test)

pickle.dump(clf, open('model.pkl', 'wb'))

pickle.dump(word_dict, open('mystrings.pkl', 'wb'))
