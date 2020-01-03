
import multiprocessing as mp

class Route:

    def __init__(self, routeString=""):
        self.routeString = routeString
        self.cartesianCoords = []

        print("Calculating route...")

        currentCoord = (0,0)
        route = routeString.split(",")
        for move in route:
            direction = move[0]
            distance = int(move[1:])

            for x in range(distance):
                if direction == "L":
                    currentCoord = (currentCoord[0] - 1, currentCoord[1])
                elif direction == "R":
                    currentCoord = (currentCoord[0] + 1, currentCoord[1])
                elif direction == "U":
                    currentCoord = (currentCoord[0], currentCoord[1] + 1)
                elif direction == "D":
                    currentCoord = (currentCoord[0], currentCoord[1] - 1)

                self.cartesianCoords.append(currentCoord)

        print("Route has " + str(len(self.cartesianCoords)) + " coordinates")

    def get_coords(self):
        return self.cartesianCoords

    def get_signal_delay(self, coord):
        return self.cartesianCoords.index(coord)

class IntersectionFinder:
    def __init__(self, routes=[]):
        self.routes = routes

    def find_intersections(self):
        route1Coords = self.routes[0].get_coords()
        route2Coords = self.routes[1].get_coords()

        pool = mp.Pool(mp.cpu_count())
        intersections = [pool.apply(self.find_intersections_mp, args=(route1Coords[i], i, route2Coords)) for i in range(len(route1Coords)) ]
        pool.close()

        flat_list = [item for sublist in intersections for item in sublist]
        return flat_list


    def find_intersections_mp(self, coord, index, coords):
        intersections = []
        for i in range(len(coords)):
            coord2 = coords[i]

            if coord == coord2:
                manhattan = abs(coord[0]) + abs(coord[1])
                signalDelay = index + i + 2
                print("Found a match: " + str(coord) + ", manhattan distance is " + str(
                    manhattan) + ", signal delay is " + str(signalDelay))
                intersections.append((coord, manhattan, signalDelay))

        return intersections



    def find_shortest_manhattan_distance(self):
        intersections = sorted(self.find_intersections(), key=lambda x: x[1])
        return intersections[0][1]

    def find_shortest_signal_delay(self):
        intersections = sorted(self.find_intersections(), key=lambda x: x[2])
        return intersections[0][2]

if __name__ == '__main__':
    routes = []
    file = open("../../resources/day3/input.txt")
    for line in file:
        routes.append(Route(line))
    file.close()

    # print(IntersectionFinder(routes).find_shortest_manhattan_distance())
    print(IntersectionFinder(routes).find_shortest_signal_delay())
