# this imports the class Animal (methods included) from the Revision.py module

# Abstraction - using class Animal
from Revision.Revision import Animal

Animal3 = Animal("Snake", "Jake", 9)

Animal3.eat()

# Inheritance - using class Animal

from Revision.Revision import Animal

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(type, name, age)

    def sleep(self):
        print("{} is sleeping. zZZ".format(self.name))


Reptile1 = Reptile("Gary", 15)

Reptile1.sleep()        # method from new Reptile class
Reptile1.eat()          # method from Animal class
