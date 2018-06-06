# MDImpute.py
# Chu Luo
import numpy as np
from scipy import stats
from sklearn import *

# first, mode, mean, median, hot deck impute.

def mean_impute(inputSet, column_id, label):
    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:,column_id] != missing_label]

    # get mean of complete rows

    mean = np.mean(valid_set[:,column_id])

    a[a[:, column_id] == missing_label,column_id ] = mean

    return a

def median_impute(inputSet, column_id, label):
    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:, column_id] != missing_label]

    # get median of complete rows

    median = np.median(valid_set[:, column_id])

    a[a[:, column_id] == missing_label, column_id] = median

    return a

def mode_impute(inputSet, column_id, label):
    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:, column_id] != missing_label]

    mode, count = stats.mode(valid_set[:, column_id])

    a[a[:, column_id] == missing_label, column_id] = mode

    return a

def hot_deck_impute(inputSet, column_id, label):
     missing_label = int(label)
     a = np.array(inputSet)
     rows = len(a)
     last_observation = -1
     for i in range(rows):
         if a[i, column_id] == label:
             a[i, column_id] = last_observation
             # make sure a[0,column_id] is not missing
         else:
             last_observation = a[i, column_id]
     return a


def lr_impute(inputSet, column_id, label):
    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:, column_id] != missing_label]
    invalid_set = a[a[:, column_id] == missing_label]

    X_train = np.delete(valid_set, column_id, 1)

    Y_train = valid_set[:,column_id]

    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, Y_train)

    X_test = np.delete(invalid_set, column_id, 1)

    Y_test = regr.predict(X_test)

    rows = len(a)
    imputation_count = 0
    for i in range(rows):
        if a[i, column_id] == label:
            a[i, column_id] = Y_test[imputation_count]
            imputation_count = imputation_count + 1

    return a

def knn_impute(inputSet, column_id, label):
    # normalization needed
    
    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:, column_id] != missing_label]
    invalid_set = a[a[:, column_id] == missing_label]

    X_train = np.delete(valid_set, column_id, 1)

    Y_train = valid_set[:, column_id]

    regr = neighbors.KNeighborsRegressor( n_neighbors=10)

    # Train the model using the training sets
    regr.fit(X_train, Y_train)

    X_test = np.delete(invalid_set, column_id, 1)

    Y_test = regr.predict(X_test)

    rows = len(a)
    imputation_count = 0
    for i in range(rows):
        if a[i, column_id] == label:
            a[i, column_id] = Y_test[imputation_count]
            imputation_count = imputation_count + 1

    return a

def MLP_impute(inputSet, column_id, label):
    # normalization needed

    missing_label = int(label)
    a = np.array(inputSet)
    valid_set = a[a[:, column_id] != missing_label]
    invalid_set = a[a[:, column_id] == missing_label]

    X_train = np.delete(valid_set, column_id, 1)

    Y_train = valid_set[:, column_id]

    regr = neural_network.MLPRegressor()

    # Train the model using the training sets
    regr.fit(X_train, Y_train)

    X_test = np.delete(invalid_set, column_id, 1)

    Y_test = regr.predict(X_test)

    rows = len(a)
    imputation_count = 0
    for i in range(rows):
        if a[i, column_id] == label:
            a[i, column_id] = Y_test[imputation_count]
            imputation_count = imputation_count + 1

    return a
# finally, our feature impact impute

# test

a = np.array([[1, 2, 5], [6, 6, -1], [6, 6, 5], [6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6],[6, 6, 6], [6, 6, -1]], dtype='f')

print(a)

b = MLP_impute(a, 2, -1)

print(b)
