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
print(sh)