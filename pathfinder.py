import sys

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
        self.process(self.origin, 0)
    
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

    def process(self, current_location, current_distance):
        
        if(self.end_processing):
            return
        change = self.data[current_location[0]][current_location[1]].assign_distance(current_distance)
        if(not(change)):
            return
        if(current_location == self.destination):
            self.end_processing = True
            return
        neighbourhood = self.neighbour_points(current_location)
        for i in neighbourhood:
            self.process(i.location, current_distance + 1)
    
    def neighbour_points(self, location):
        
        neighbour_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0):
                    neighbour_list.append(self.data[i][j])
                else:
                    pass
        neighbour_list.remove(self.data[location[0]][location[1]])
        return neighbour_list

class point(object):

    def __init__(self, location, passable):

        self. location = location
        self.passable = passable
        self.distance_origin = None
        self.distance_destination = None
    
    def assign_distance(self, distance):

        if(self.passable and self.distance_origin == None):
            self.distance_origin = distance
            return True
        return False

pathfinder()
