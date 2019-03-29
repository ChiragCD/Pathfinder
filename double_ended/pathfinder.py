import sys, pickle, pg

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
        self.midpoint = []
        self.destination = []
        self.distance = []
        self.considered_points = []
        self.path = []
        self.__main__()

    def __main__(self):

        self.consider_args()
        self.get_data()
        self.get_locations()
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
        data = pickle.load(file)
        file.close()
        self.box_size = len(data)
        self.data = data
        self.distance = [[0 for i in range(self.box_size)] for j in range(self.box_size)]           ## Assumes square map
        pg.show_map(data, [])

    def get_locations(self):

        if(not(self.origin)):
            self.origin = [int(i) for i in input("Origin >> ").split()]
        if(not(self.destination)):
            self.destination = [int(i) for i in input("Destination >> ").split()]
        if(not(self.data[self.origin[0]][self.origin[1]]) or not(self.data[self.destination[0]][self.destination[1]])):
            print("Not possible")

    def process_handler(self):

        self.distance[self.origin[0]][self.origin[1]] = 1
        self.distance[self.destination[0]][self.destination[1]] = -1
        process_queue_origin = self.important_neighbour_points(self.origin, 1)
        process_queue_destination = self.important_neighbour_points(self.destination, -1)
        distance = 1
        new_process_queue_origin = []
        new_process_queue_destination = []
        while(not(self.end_processing)):
            distance += 1
            self.process(distance, process_queue_origin)
            self.process((-1 * distance), process_queue_destination)
            for i in process_queue_origin:
                new_process_queue_origin = unique_merge(new_process_queue_origin, self.important_neighbour_points(i, 1))
            for i in process_queue_destination:
                new_process_queue_destination = unique_merge(new_process_queue_destination, self.important_neighbour_points(i, -1))
            process_queue_origin = new_process_queue_origin + []
            process_queue_destination = new_process_queue_destination + []
            new_process_queue_origin = []
            new_process_queue_destination = []
            if(not(process_queue_origin) or not(process_queue_destination)):
                break
            pg.show_map(self.data, self.considered_points)
        print("Distance - ", distance)

    def process(self, distance, process_queue):

        for location in process_queue:
            self.considered_points.append((location[0], location[1]))
            if(self.distance[location[0]][location[1]] == 0):
                self.distance[location[0]][location[1]] = distance
            else:
                self.end_processing = True
                if(distance > 0):
                    self.shortest_distance = distance - self.distance[location[0]][location[1]] - 2
                else:
                    self.shortest_distance = self.distance[location[0]][location[1]] - distance - 2
                self.midpoint = location
                print(self.midpoint)
                break
    
    def important_neighbour_points(self, location, reference):
        
        neighbour_list = []
        for i in [location[0] - 1, location[0], location[0] + 1]:
            for j in [location[1] - 1, location[1], location[1] + 1]:
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j]):
                    if(reference == 1 and self.distance[i][j] < 1):
                        neighbour_list.append([i, j])
                    elif(reference == -1 and self.distance[i][j] > -1):
                        neighbour_list.append([i, j])
        return neighbour_list

    def set_path(self):
        
        location = self.midpoint
        self.path = [tuple(self.origin), tuple(self.destination)]
        sign = self.distance[self.midpoint[0]][self.midpoint[1]] / abs(self.distance[self.midpoint[0]][self.midpoint[1]])
        if(sign == 1):
            while(self.origin != location): 
                self.path.append((location[0], location[1]))
                for i in self.vicinity(location):
                    if(self.distance[i[0]][i[1]] == self.distance[location[0]][location[1]] - 1):
                        location = i
                        break
            location = self.midpoint
            self.distance[location[0]][location[1]] = -1 - self.distance[location[0]][location[1]]
            while(self.destination != location):
                self.path.append((location[0], location[1]))
                for i in self.vicinity(location):
                    if(self.distance[i[0]][i[1]] == self.distance[location[0]][location[1]] + 1):
                        location = i
                        break
        else:
            while(self.destination != location):
                self.path.append((location[0], location[1]))
                for i in self.vicinity(location):
                    if(self.distance[i[0]][i[1]] == self.distance[location[0]][location[1]] + 1):
                        location = i
                        break
            location = self.midpoint
            self.distance[location[0]][location[1]] *= -1
            while(self.origin != location):
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
                if(i < self.box_size and j < self.box_size and i >= 0 and j >= 0 and self.data[i][j] != 0):
                    if(self.distance[i][j] != 0):
                        vicinity_list.append([i, j])
        return vicinity_list
    
pathfinder()
