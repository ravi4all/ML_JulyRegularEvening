import math
import csv
import random

def load_dataset(filename):
    dataset = []
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
            
    return dataset

def str_to_float(dataset):
    
    for i in range(len(dataset)):
        for j in range(len(dataset[0])):
            dataset[i][j] = float(dataset[i][j])

def minmax(dataset):
    
    minmax = []
    
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        minVal = min(col_values)
        maxVal = max(col_values)
        minmax.append([minVal, maxVal])
        
    return minmax

def normalization(dataset):
    numer = 0
    denom = 0
    for row in dataset:
        for col in range(len(row)):
            numer = col - minmaxData[col][0]
            denom = minmaxData[col][1] - minmaxData[col][0]
            row[col] = numer/denom

def accuracy_metrics(actual, predicted):
    count = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            count += 1
    
    return count / len(actual) * 100

def predictions(row,coef):
    ypred = coef[0]
    for i in range(len(row) - 1):
        ypred += coef[i+1] * row[i]  
    return 1 / (1 + math.exp(-ypred))

# train test split
def cross_validation(n_folds, dataset):
    datasetCopy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    folds = []
    
    for i in range(n_folds):
        fold = []
        
        while len(fold) < fold_size:
            index = random.randrange(len(datasetCopy))
            fold.append(datasetCopy.pop(index))
        folds.append(fold)
    
    return folds

def evaluateAlgorithm(dataset, n_folds, algorithm, nb_epoch, learning_rate):
    scores = []
    
    folds = cross_validation(n_folds, dataset)
    
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train, [])
        test = []
        for row in fold:
            rowcopy = list(row)
            rowcopy[-1] = None
            test.append(rowcopy)
            
        actual = [row[-1] for row in fold]
        predicted = algorithm(train, test, learning_rate, nb_epoch)
        
        score = accuracy_metrics(actual, predicted)
        scores.append(score)
        
    return scores
        
def sgd_logistic(dataset, learning_rate, nb_epoch):
    b = [0] * nb_epoch
    
    for epoch in range(nb_epoch):
        for row in dataset:
            yhat = predictions(row,b)
            loss = row[-1] - yhat
            b[0] = b[0] + learning_rate * loss * yhat * (1 - yhat)
            for i in range(len(row) - 1):
                b[i+1] = b[i+1] + learning_rate * loss * yhat * (1-yhat) * row[i]
    return b

def logisticRegression(train, test, learning_rate, nb_epoch):
    y_pred = []
    coef = sgd_logistic(train, learning_rate, nb_epoch)
    for row in test:
        pred = predictions(row, coef)
        pred = round(pred)
        y_pred.append(pred)
        
    return y_pred

filename = 'pima-indians-diabetes.data.csv'
dataset = load_dataset(filename)
str_to_float(dataset)
minmaxData = minmax(dataset)
normalization(dataset)

n_folds = 5
nb_epoch = 1000
learning_rate = 0.01
accuracy = evaluateAlgorithm(dataset, n_folds, logisticRegression, nb_epoch, learning_rate)
print(accuracy)