# MDImpute.py
# Chu Luo
import numpy as np
from scipy import stats

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





# then regression impute

# finally, our feature impact impute

# test

a = np.array([[1, 2, 5], [3, 4, -1], [6, 6, 5],[6, 6, 6], [1, 9, -1]], dtype='f')

b = hot_deck_impute(a,2,-1)

print(b)
