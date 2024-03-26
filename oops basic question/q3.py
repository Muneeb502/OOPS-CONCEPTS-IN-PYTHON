""""
3. Write a Python program that creates a class called 'Vehicle' with properties for 
make, model, and year. Include a method to display vehicle details. Create a 
subclass called 'Car' that inherits from the 'Vehicle' class and includes an 
additional property for the number of doors. Override the display method to 
include the number of doors.

"""

class vehicle:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
    def car_deatail(self):
        print(f"""
              make = {self.make}
              model = {self.model}
              year = {self.year}
              """)
class car(vehicle):
    def __init__(self,make,model,year,door) -> None:
        super(). __init__(make,model,year)
        self.door = door
    def car_deatail(self):
         super().car_deatail()
         print(f"door = {self.door}")

c1 = car("KIA","SORTAGE","2023","four door")
c1.car_deatail()