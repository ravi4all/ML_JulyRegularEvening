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
    fold_size = len(dataset) / n_folds
    folds = []
    
    for i in range(n_folds):
        fold = []
        
        while len(fold) <= fold_size:
            index = random.randrange(len(datasetCopy))
            fold.append(datasetCopy.pop(index))
        folds.append(fold)
    
    return folds

def evaluateAlgorithm(dataset, n_folds, algorithm):
    scores = []
    
    folds = cross_validation(n_folds, dataset)
    
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        
        test = []
        for row in fold:
            rowcopy = row
            rowcopy[-1] = None
            test.append(rowcopy)
            
        actual = [row[-1] for row in fold]
        predicted = algorithm()
        
        score = accuracy_metrics(actual, predicted)
        scores.append(score)
        
    return scores
        
        

def sgd_logistic():
    pass

def logisticRegression():
    pass

filename = 'pima-indians-diabetes.data.csv'
dataset = load_dataset(filename)
str_to_float(dataset)
minmaxData = minmax(dataset)
normalization(dataset)



