import sys, pickle, pg
from zeros import zero

def unique_merge(l1, l2):

    for i in l2:
        if i not in l1:
            l1.append(i)
    return l1

class pathfinder(object):

    def __init__(self):

        self.end_processing = False
        self.midpoint = None
        self.box_size = 0
        self.shortest_distance = -1
        self.dimension = 2                                  ## Change Here
        self.data_source = "pathfinderdata.bin"
        self.data = []
        self.origin = []
        self.destination = []
        self.distance = []
        self.considered_points = []
        self.path = []
        self.__main__()

    def __main__(self):

        self.consider_args()
        self.get_data()
        self.get_locations()
        self.set_distance(self.origin, 0)
        self.process_handler()
        if(self.end_processing):
            print("Possible", self.shortest_distance)
        else:
            print("Not possible", self.shortest_distance)
        self.set_path()
    
    def consider_args(self):

        for i in sys.argv[1:]:
            if(i[:3] == "-f="):
                self.datasource = i[3:]
            if(i[:3] == "-o="):
                self.origin = [int(j) for j in i[3:].split(',')]
            if(i[:3] == "-d="):
                self.destination = [int(j) for j in i[3:].split(',')]
                
    def get_data(self):

        file = open(self.data_source, 'rb')
        self.data = pickle.load(file)
        file.close()
        self.box_size = len(self.data)
        self.distance = zero(self.dimension, self.boxsize)           ## Assumes square map

    def get_locations(self):

        if(not(self.origin)):
            self.origin = [int(i) for i in input("Origin >> ").split()]
        if(not(self.destination)):
            self.destination = [int(i) for i in input("Destination >> ").split()]

    def set_distance(self, location, distance):

        current_dimension = 0
        element = self.distance[location[currentdimension]]
        while(current_dimension < self.dimension):
            element = element[location[currentdimension]]
            current_dimension += 1
        

    def process_handler(self):

        process_queue = self.important_neighbour_points(self.origin)
        distance = 0
        new_process_queue = []
        while(not(self.end_processing)):
            distance += 1
            self.process(distance, process_queue)
            for i in process_queue:
                new_process_queue = unique_merge(new_process_queue, self.important_neighbour_points(i))
            process_queue = new_process_queue + []
            new_process_queue = []
            if(not(process_queue)):
                break
            pg.show_map(self.data, self.considered_points)
        print("Distance - ", distance)

    def process(self, distance, process_queue):

        if(self.destination in process_queue):
            self.shortest_distance = distance
            self.end_processing = True
            self.considered_points.append(tuple(self.destination))
            self.distance[self.destination[0]][self.destination[1]] = distance
            return
        for location in process_queue:
            self.distance[location[0]][location[1]] = distance
            self.considered_points.append((location[0], location[1]))
    
    def important_neighbour_points(self, location):
        
        neighbour_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j]):
                    if(self.distance[i][j] == -1):
                        neighbour_list.append([i, j])
        return neighbour_list

    def set_path(self):
        
        location = self.destination
        while(location != self.origin):
            self.path.append((location[0], location[1]))
            for i in self.vicinity(location):
                if(self.distance[i[0]][i[1]] == self.distance[location[0]][location[1]] - 1):
                    location = i
                    break
        pg.show_path(self.data, self.considered_points, self.path)

    def vicinity(self, location):

        vicinity_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j]):
                    if(self.distance[i][j] > -1):
                        vicinity_list.append([i, j])
        return vicinity_list
    
pathfinder()
