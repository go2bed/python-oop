import datetime


class Circle(object):
    # class object attributes
    pi = 3.14
    today = datetime.date.today()

    def __init__(self, radius=1, perimeter=25):
        self.radius = radius
        self.perimeter = perimeter

    def area(self):
        # radius**2 * pi
        return (self.radius ** 2) * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def get_perimeter(self):
        # perimeter =  2 * pi * radius
        return 2 * Circle.pi * self.radius


c = Circle(radius=100)
c.set_radius(50)

print(c.get_radius())
print(c.area())
print(str(c.get_perimeter()) + ' this is a perimeter of the Circle')
print(Circle.today)
