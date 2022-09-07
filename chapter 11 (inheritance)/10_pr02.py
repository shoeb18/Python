class Animal:
    animalType = "mammal"
        
class Pet:
    color = "white"
        
class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
    