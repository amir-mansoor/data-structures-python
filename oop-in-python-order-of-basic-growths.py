class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

p1 = Point() 
print("p1 ",p1.x)

p2 = Point(2,4)
print("p2", p2.x)

print(p2) # here is the pointer, technically these are same things 

