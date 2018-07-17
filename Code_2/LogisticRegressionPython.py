import math
import csv
import random

def load_dataset():
    pass

def str_to_float():
    pass

def minmax():
    pass

def normalization():
    pass

def cross_validation():
    pass

def accuracy_metrics():
    pass

def predictions(row,coef):
    ypred = coef[0]
    for i in range(len(row) - 1):
        ypred += coef[i+1] * row[i]    
    return 1 / (1 + math.exp(-ypred))

def evaluateAlgorithm():
    pass

def sgd_logistic():
    pass

def logisticRegression():
    pass

