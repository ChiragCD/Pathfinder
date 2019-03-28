import random, pickle

boxsize = 10
data = [[0 for i in range(boxsize)] for j in range(boxsize)]

for i in range(boxsize):
    for j in range(boxsize):
        data[i][j] = random.randint(0, 1)

def display_map():
    for i in range(boxsize):
        for j in range(boxsize):
            print(data[i][j], end = ' ')
        print('\n')

file = open("pathfinderdata.bin", 'wb')
pickle.dump(data, file)
file.close()
