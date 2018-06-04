# MDImpute.py
# Chu Luo
import numpy as np

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

    # get mean of complete rows

    median = np.median(valid_set[:, column_id])

    a[a[:, column_id] == missing_label, column_id] = median

    return a

def mode_impute(inputSet, column_id, label):
    missing_label = int(label)

def hot_deck_impute(inputSet, column_id, label):
     missing_label = int(label)


# then regression impute

# finally, our feature impact impute

# test

a = np.array([[1, 2, -1], [3, 4, 5], [6, 6, 61],[6, 6, 6], [1, 9, -1]], dtype='f')

b = median_impute(a,2,-1)

print(b)
