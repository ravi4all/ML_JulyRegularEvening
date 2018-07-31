# os - operating system
import os
# io - input/output
import io
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def readFile(path):
    for root, folder, files in os.walk(path):
        for fileName in files:
            file = os.path.join(root, fileName)

            inBody = False
            lines = []
            f = io.open(file, 'r', encoding='latin1')
            for line in f:
                #     print(line)
                if inBody == True:
                    lines.append(line)
                #         print(lines)
                elif line == "\n":
                    inBody = True
            f.close()
            message = "\n".join(lines)
            yield message, path


def buildDataFrame(path, classification):
    row = []
    index = []

    for message, filename in readFile(path):
        row.append({'message': message, "class": classification})
        index.append(filename)

    return pd.DataFrame(data=row, index=index)

dataset = pd.DataFrame({'message':[], 'class':[]})

dataset = dataset.append(buildDataFrame('emails/spam', 'spam'))
dataset = dataset.append(buildDataFrame('emails/ham', 'ham'))

vect = CountVectorizer()
X_train = vect.fit_transform(dataset['message'].values)
y = dataset['class'].values

x_train, x_test, y_train, y_test = train_test_split(X_train, y, test_size=0.2)

nb = MultinomialNB()
nb.fit(x_train, y_train)

def classify(inputData):
    inputData = vect.transform([inputData])
    pred = nb.predict(inputData)

    return pred