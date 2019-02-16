import random

boxsize = 400
data = ''

for i in range(boxsize):
    for j in range(boxsize):
        data += str(random.randint(0, 1)).rjust(4)
    data += '\n'

print(data)

file = open("pathfinderdata.txt", 'w')
file.write(data)
file.close()
