##### Problem 1 #####

import math


class Line:

    def __init__(self, coor1, coor2):
        
        self.tuple1 = coor1
        self.tuple2 = coor2

    def distance(self):
        
        result = math.sqrt(((self.tuple2[0] - self.tuple1[0])**2) + ((self.tuple2[1] - self.tuple1[1])**2))

        return result 

    def slope(self):
        
        result = (self.tuple2[1] - self.tuple1[1])/(self.tuple2[0] - self.tuple1[0])

        return result

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(f"The distance between your points is {li.distance()}")

print(f"The slope between your points is {li.slope()}")