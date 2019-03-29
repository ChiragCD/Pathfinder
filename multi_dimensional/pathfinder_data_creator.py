import random, pickle

class data(object):
        
    def create(self, dimension, boxsize):

        if(dimension - 1):
            return[data().create(dimension - 1, boxsize) for i in range(boxsize)]
        else:
            return [random.randint(0, 1) for i in range(boxsize)]

boxsize = 10
dimension = 4

data = data().create(dimension, boxsize)

print(data)

file = open("pathfinderdata.bin", 'wb')
pickle.dump(data, file)
file.close()
