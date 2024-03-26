""""
2. Write a Python program to create a class called 'Rectangle' with properties for 
width and height. Include two methods to calculate rectangle area and perimeter. 
Create an instance of the 'Rectangle' class and calculate its area and perimeter. 

"""


class rectangle():
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def area(self):
        print(f"So the area of Rectangle is {self.width*self.height}") 
    def perimeter(self):
        print(f"so the perimeter of rectangle is {2*(self.height+self.width)}")
        
R = rectangle(4,6)
R.area()
R.perimeter()