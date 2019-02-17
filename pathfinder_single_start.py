import sys

def unique_merge(l1, l2):

    for i in l2:
        if i not in l1:
            l1.append(i)
    return l1

class pathfinder(object):

    def __init__(self):

        self.end_processing = False
        self.box_size = 0
        self.data_source = "pathfinderdata.txt"
        self.data = []
        self.origin = []
        self.destination = []
        self.__main__()

    def __main__(self):

        self.consider_args()
        self.get_data()
        self.get_locations()
        self.data[self.origin[0]][self.origin[1]].distance_origin = 0
        self.process_handler()
        if(self.end_processing):
            print("Possible")
        else:
            print("Not possible")
    
    def consider_args(self):

        for i in sys.argv[1:]:
            if(i[:3] == "-f="):
                self.datasource = i[3:]
            if(i[:3] == "-o="):
                self.origin = [int(j) for j in i[3:].split(',')]
            if(i[:3] == "-d="):
                self.destination = [int(j) for j in i[3:].split(',')]
                
    def get_data(self):

        file = open(self.data_source, 'r')
        data = file.readlines()
        file.close()
        self.box_size = len(data)
        self.data = [[None for i in range(self.box_size)] for j in range(self.box_size)]           ## Assumes square map
        for i in range(len(data)):
            for j in range(len(data[i].split())):
                self.data[i][j] = point([i, j], bool(int(data[i].split()[j].strip())))

    def get_locations(self):

        if(not(self.origin)):
            self.origin = [int(i) for i in input("Origin >> ").split()]
        if(not(self.destination)):
            self.destination = [int(i) for i in input("Destination >> ").split()]

    def process_handler(self):

        process_queue = self.important_neighbour_points(self.origin)
        distance = 1
        new_process_queue = []
        while(not(self.end_processing)):
            self.process(distance, process_queue)
            distance += 1
            for i in process_queue:
                new_process_queue = unique_merge(new_process_queue, self.important_neighbour_points(i.location))
            process_queue = new_process_queue + []
            new_process_queue = []
            if(not(process_queue)):
                break
        print("Distance - ", distance)

    def process(self, distance, process_queue):

        for i in process_queue:
            i.assign_distance(distance)
            if(i.location == self.destination):
                self.end_processing = True
                return
    
    def important_neighbour_points(self, location):
        
        neighbour_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j].distance_origin == None and self.data[i][j].passable):
                    neighbour_list.append(self.data[i][j])
        return neighbour_list

class point(object):

    def __init__(self, location, passable):

        self. location = location
        self.passable = passable
        self.distance_origin = None
        self.distance_destination = None
    
    def assign_distance(self, distance):

        if(self.distance_origin == None):
            self.distance_origin = distance

pathfinder()