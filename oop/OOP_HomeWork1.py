import math


class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0]) ** 2
                         + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) \
               / (self.coor2[0] - self.coor1[0])

    def __str__(self):
        return self.distance()


li = Line((3, 2), (8, 10))

print('coordinate 1 = ' + str(li.coor1))
print('coordinate 2 = ' + str(li.coor2))

print(li.distance())
print(li.slope())
