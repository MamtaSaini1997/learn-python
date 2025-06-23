# define a circle class to create a circle with radius r using the constructor.
# define an area() method of the class which calculate the area of the circle.
# define a parameter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self , radius):
        self.radius = radius
    
    def cal_area(self):
        Area = 3.14 * (self.radius * self.radius)
        print(Area)

    def cal_parameter(self):
        Parameter = 2 * 3.14 * (self.radius)
        print(Parameter)

a = Circle(3)
a.cal_area()

b = Circle(2)
b.cal_parameter()