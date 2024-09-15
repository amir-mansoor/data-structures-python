class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    # def get_human_readable(self):
    #     return "[" + str(self.x) + "," + str(self.y) + "]"

# p1 = Point() 
# print("p1 ",p1.x)

# p2 = Point(2,4)
# print("p2", p2.x)

# print(p2) # here is the pointer, technically these are same things
# print(p2.get_human_readable())



# *********** Composition *************

class Shape:
    def __init__(self,points):
        self.points = points

    def __str__(self):
        ret = ""
        for i in self.points:
            ret += str(i) + " - "

        return ret

p1 = Point(5,1)
p2 = Point(2,3)
p3 = Point(23,12)

p = [p1,p2,p3]
sh = Shape(p)
# print(sh)

# we can add methods to class after it has been defined 

def print_points(self):
    for i in self.points:
        print(i)

Shape.print_points = print_points

# sh.print_points()

# ************* Inheritence **********

# syntax is slightly different but quite easy

class Triangle(Shape):
    pass

t = Triangle(p)

# t.print_points()

def get_area(self):
    vertices = self.points
    n = len(vertices)
    a = 0.0

    for i in range(n):
        j = (i * 1) % n
        a += abs(vertices[i].x * vertices[j].y - vertices[j].x * vertices[i].y)

    return a / 2.0

Triangle.get_area = get_area
# print(t.get_area())

# ****** Overridden methods ***********

class Rectangle:
    def __init__(self,length,width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return "L: " + str(self.length) + " W: " + str(self.width)

rect = Rectangle(2,4)
# print(rect)

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

    def __str__(self):
        return "Square " + super().__str__()

square = Square(5)
print(square)
print(square.area())