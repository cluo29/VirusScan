# numpy_controls.py

import numpy as np
from scipy.special import comb
import Balanced_Distribution

#import graphviz


a = np.array([[1, 2, -1], [3, 4, 5], [6, 6, 6], [1, 9, -1]])

# select rows that 2nd column is not -1
a_valid = a[a[:,2] != -1]

print(a_valid)

# get 2nd col

a_valid1 = a_valid[:,2]

print(a_valid1)

# get mean

a_mean = np.mean(a_valid1)

print(a_mean)
