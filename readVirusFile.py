# readVirusFile.py
# Chu Luo (https://github.com/cluo29)
# v1.1

import numpy as np

# Chu does not know if label is one
features = 479



def read_one_file(filename):

    #max_id = 0

    file1 = open(filename, "r")
    # And for reading use
    lines = file1.readlines()
    file1.close()

    rows = len(lines)

    print('rows = ', rows)

    outputX = np.zeros((rows, features), dtype=int)

    outputY = []

    for i in range(rows):
        currrent_line = lines[i]

        line_items = currrent_line.split()

        num_items = len(line_items)

        for j in range(num_items):
            if j == 0:
                prob = float(line_items[j])
                if prob > 0.5:
                    outputY.append(1)
                else:
                    outputY.append(0)
            else:
                item = line_items[j]
                item_split = item.split(':')
                feature_id = int(item_split[0])

                #if feature_id>max_id:
                #    max_id = feature_id

                feature_value = int(item_split[1])
                outputX[i, feature_id] = feature_value

    #print('outputX')
    #print(outputX)

    outputY = np.array(outputY).astype(int)
    return outputX, outputY





setX, setY = read_one_file('2010-11.txt')
setX2, setY2 = read_one_file('2010-12.txt')

AllX = np.concatenate((setX, setX2), axis=0)
AllY = np.concatenate((setY, setY2), axis=0)

setX2, setY2 = read_one_file('2011-01.txt')

AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)

setX2, setY2 = read_one_file('2011-02.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-03.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-04.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-05.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-06.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-07.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-08.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-09.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-10.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-11.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2011-12.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-01.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-02.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-03.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-04.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-05.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-06.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-07.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-08.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-09.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-10.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-11.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2012-12.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-01.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-02.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-03.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-04.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-05.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-06.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-07.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-08.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-09.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-10.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-11.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2013-12.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-01.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-02.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-03.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-04.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-05.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-06.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)
setX2, setY2 = read_one_file('2014-07.txt')
AllX = np.concatenate((AllX, setX2), axis=0)
AllY = np.concatenate((AllY, setY2), axis=0)




np.savetxt("AllX.csv", AllX, delimiter=",", fmt='%i')
np.savetxt("AllY.csv", AllY, delimiter=",", fmt='%i')

"""

read_one_file('2011-01.txt')
read_one_file('2011-02.txt')
read_one_file('2011-03.txt')
read_one_file('2011-04.txt')
read_one_file('2011-05.txt')
read_one_file('2011-06.txt')
read_one_file('2011-07.txt')
read_one_file('2011-08.txt')
read_one_file('2011-09.txt')
read_one_file('2011-10.txt')
read_one_file('2011-11.txt')
read_one_file('2011-12.txt')
read_one_file('2012-01.txt')
read_one_file('2012-02.txt')
read_one_file('2012-03.txt')
read_one_file('2012-04.txt')
read_one_file('2012-05.txt')
read_one_file('2012-06.txt')
read_one_file('2012-07.txt')
read_one_file('2012-08.txt')
read_one_file('2012-09.txt')
read_one_file('2012-10.txt')
read_one_file('2012-11.txt')
read_one_file('2012-12.txt')
read_one_file('2013-01.txt')
read_one_file('2013-02.txt')
read_one_file('2013-03.txt')
read_one_file('2013-04.txt')
read_one_file('2013-05.txt')
read_one_file('2013-06.txt')
read_one_file('2013-07.txt')
read_one_file('2013-08.txt')
read_one_file('2013-09.txt')
read_one_file('2013-10.txt')
read_one_file('2013-11.txt')
read_one_file('2013-12.txt')
read_one_file('2014-01.txt')
read_one_file('2014-02.txt')
read_one_file('2014-03.txt')
read_one_file('2014-04.txt')
read_one_file('2014-05.txt')
read_one_file('2014-06.txt')
read_one_file('2014-07.txt')

"""

