""""
8. Write a Python program that creates a class called 'Animal' with properties for 
species and sound. Include a method to make the animal's sound. Create a 
subclass called 'Dog' that inherits from the 'Animal' class and adds an additional 
property for color. Override the make sound method to include the dog's color. 
Create an instance of the 'Dog' class and make it make its sound. 

"""

class Animal():
    def __init__(self,species,sound) -> None:
        self.species = species
        self.sound = sound