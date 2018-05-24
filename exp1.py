# exp1.py
#
# Chu Luo


from numpy import genfromtxt
import numpy as np



def make_random_missing (inputSet, column, rate_of_missing=0.1):
    rows = len(inputSet)
    # so 0, ... ,  rows-1 are good to choose
    # we choose rate * len ones
    # a = np.random.choice(5, 4, replace=False)
    # will get 0-4
    # unique ones! by using False

    outputSet = inputSet

    missing_count = int(np.floor(rate_of_missing * rows))

    print('missing_count = ', missing_count)

    missing_rows = np.random.choice(rows, missing_count, replace=False)

    for i in missing_rows:
        outputSet[i,column] = int(-1)

    return outputSet




np.random.seed(0)


trainX = genfromtxt('2010-2013X.csv', delimiter=',')

print(trainX)

print(len(trainX))

trainY = genfromtxt('2010-2013Y.csv', delimiter=',')

print(trainY)

print(len(trainY))

testX = genfromtxt('2014X.csv', delimiter=',')

print(testX)

print(len(testX))

testY = genfromtxt('2014Y.csv', delimiter=',')

print(testY)

print(len(testY))

# make missing values in  feature number 21, (20) in python
# test set


#outputSet = make_random_missing(testX, 20)

#print(outputSet)

#np.savetxt("testMissX.csv", outputSet, delimiter=",", fmt='%i')
