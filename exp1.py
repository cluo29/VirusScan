# exp1.py
#
# Chu Luo


from numpy import genfromtxt
import numpy as np
import feature_impact


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

testY = testY.reshape(testY.shape[0],-1)

print(testY)

print(len(testY))

# make missing values in  feature number 21, (20) in python
# test set


#outputSet = make_random_missing(testX, 20)

#print(outputSet)

#np.savetxt("testMissX.csv", outputSet, delimiter=",", fmt='%i')

detector = feature_impact.Detector_C(2, tree_max=200)

# feature values
X_train = trainX

# class labels
Y_train = trainY

# 0 is timestamp of training set
detector.train(X_train,Y_train,0)

FI_output = detector.get_FI()

print("FI_list =")
print(FI_output)

#

testXItem=testX[0]
testXItem=np.array([testXItem])

testYItem=testY[0]
testYItem=np.array([testYItem])

FI_list = detector.measure_FI(testXItem ,testYItem ,5)

print("FI_change =")
print(FI_list)




"""
dict['Name']

X_train2 = np.array([[0,0,0,0],[0,0,1,0]])

Y_train2 = np.array([2,1])

# 5 is timestamp of test set
FI_list = detector.measure_FI(X_train2,Y_train2,5)

print("FI_list = ", FI_list)

"""
