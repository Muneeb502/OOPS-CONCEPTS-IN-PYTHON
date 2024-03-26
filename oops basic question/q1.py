""""
1. Write a Python program to create a class called "Person" with properties for 
name, age and country. Include a method to display the person's details. Create 
two instances of the 'Person' class and display their details. 

"""



class person:
    def __init__(self,name,age,country) -> None:
        self.name = name
        self.age = age
        self.country = country
    def detail(self):
        print(f"the name of person is {self.name} and age is {self.age} and from {self.country}")
p1 = person("manzoor",34,"pakistan")
p2 = person("ahmed",23,"america")

p1.detail()
p2.detail()                  