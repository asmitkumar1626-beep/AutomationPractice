class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("The area of rectangle is",self.length * self.breadth)
rect1=Area(2,4)
rect1.area()