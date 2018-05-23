# Virustest.py
# Chu Luo (https://github.com/cluo29)
# v1.0


filename = '2010-11.txt'


file1 = open(filename,"r")
# And for reading use
lines = file1.readlines()
file1.close()


rows = len(lines)

print('rows = ', rows)

dog = lines[0]

print(dog)



cjjawl = dog.split()

print(cjjawl)

prob = None

row_items = len(cjjawl)

print('row_items')

print(row_items)

feature_name = []

feature_value = []

for i in range(row_items):
    if i == 0:
        prob = cjjawl[i]
    else:
        item = cjjawl[i]
        print(item)
        item_split = item.split(':')
        print(item_split[0])
        print(item_split[1])

print(prob)

#print(lines[1])

#print(lines[2])

#print(lines[rows-1])

#for i in lines:
   # print(i)
