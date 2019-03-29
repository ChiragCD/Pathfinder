class zero(object):
        
    def create(self, dimension, boxsize):

        if(dimension - 1):
            return[zero().create(dimension - 1, boxsize) for i in range(boxsize)]
        else:
            return [0 for i in range(boxsize)]

def zeros(dimension, boxsize):

    return zero().create(dimension, boxsize)
