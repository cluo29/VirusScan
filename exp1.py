# exp1.py
#
# Chu Luo


from numpy import genfromtxt


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

