import sys, pickle

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
        self.data_source = "pathfinderdata.bin"
        self.data = []
        self.origin = []
        self.destination = []
        self.path = []
        self.__main__()

    def __main__(self):

        self.consider_args()
        self.get_data()
        self.get_locations()
        self.data[self.origin[0]][self.origin[1]].distance_origin = 0
        self.process_handler()
        if(self.end_processing):
            print("Possible", self.shortest_distance)
        else:
            print("Not possible", self.shortest_distance)
    
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
        data = pickle.load(file)
        file.close()
        self.box_size = len(data)
        self.data = [[None for i in range(self.box_size)] for j in range(self.box_size)]           ## Assumes square map
        for i in range(len(data)):
            for j in range(len(data[i].split())):
                self.data[i][j] = point([i, j], data[i][j])

    def get_locations(self):

        if(not(self.origin)):
            self.origin = [int(i) for i in input("Origin >> ").split()]
        if(not(self.destination)):
            self.destination = [int(i) for i in input("Destination >> ").split()]

    def process_handler(self):

        process_queue_origin = self.important_neighbour_points(self.origin, 0)
        process_queue_destination = self.important_neighbour_points(self.destination, 1)
        distance = 0
        new_process_queue_origin = []
        new_process_queue_destination = []
        while(not(self.end_processing)):
            distance += 1
            self.process(distance, process_queue_origin, 0)
            self.process(distance, process_queue_destination, 1)
            for i in process_queue_origin:
                new_process_queue_origin = unique_merge(new_process_queue_origin, self.important_neighbour_points(i.location, 0))
            for i in process_queue_destination:
                new_process_queue_destination = unique_merge(new_process_queue_destination, self.important_neighbour_points(i.location, 1))
            process_queue_origin = new_process_queue_origin + []
            process_queue_destination = new_process_queue_destination + []
            new_process_queue_origin = []
            new_process_queue_destination = []
            if(not(process_queue_origin) or not(process_queue_destination)):
                break
        print("Distance - ", distance)

    def process(self, distance, process_queue, reference):

        for i in process_queue:
            i.assign_distance(distance, reference)
            if(i.distance_origin and i.distance_destination):
                self.end_processing = True
                self.midpoint = i
                self.shortest_distance = i.distance_origin + i.distance_destination
                return
    
    def important_neighbour_points(self, location, reference):
        
        neighbour_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j].passable):
                    if(self.data[i][j].distance_origin == None and self.data[i][j].distance_destination == None):
                        neighbour_list.append(self.data[i][j])
                    elif((reference == 0 and self.data[i][j].distance_destination) or (reference == 1 and self.data[i][j].distance_origin)):
                        neighbour_list.append(self.data[i][j])
        return neighbour_list

class point(object):

    def __init__(self, location, passable):

        self. location = location
        self.passable = passable
        self.distance_origin = None
        self.distance_destination = None
    
    def assign_distance(self, distance, reference):

        if(reference == 0 and self.distance_origin == None):
            self.distance_origin = distance
        if(reference == 1 and self.distance_destination == None):
            self.distance_destination = distance

pathfinder()
