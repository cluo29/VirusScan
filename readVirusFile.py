# readVirusFile.py
# Chu Luo (https://github.com/cluo29)
# v1.0

import numpy as np

# Chu does not know if label is one
features = 483

def read_one_file(filename):

    file1 = open(filename, "r")
    # And for reading use
    lines = file1.readlines()
    file1.close()

    rows = len(lines)

    print('rows = ', rows)

    output = np.zeros((rows,features))

    for i in range(rows):
        currrent_line = lines[i]

        print('currrent_line')

        print(currrent_line)

        break

    print(output)




filename = '2010-11.txt'

read_one_file(filename)


