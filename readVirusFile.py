# readVirusFile.py
# Chu Luo (https://github.com/cluo29)
# v1.0

import numpy as np

# Chu does not know if label is one
features = 482



def read_one_file(filename):
    max_id = 0

    file1 = open(filename, "r")
    # And for reading use
    lines = file1.readlines()
    file1.close()

    rows = len(lines)

    print('rows = ', rows)

    outputX = np.zeros((rows,features))

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
                if feature_id>max_id:
                    max_id = feature_id
                feature_value = int(item_split[1])
                outputX[i,feature_id] = feature_value

    print('outputX')
    print(outputX)

    print('outputY')
    print(outputY)

    print('max_id = ', max_id)



filename = '2010-11.txt'

read_one_file(filename)


