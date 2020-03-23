# Exercises for 23/03/20

# Exercise 1: Inheritance - create a parent class called Person then a child class called Student


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def talk(self):
        age = input("How old are you?: ")
        print("{} is {} years old".format(self.fname, age))


p1 = Person("John", "Doe")
p1.talk()


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def enjoy(self):
        hobby = input("Give me one hobby: ")
        print("{} enjoys {}".format(self.fname, hobby))

    def chill(self, beverage):
        print("{} likes a chilled {}".format(self.fname, beverage))


s1 = Student("Jane", "Doe")
s1.talk()
s1.enjoy()
s1.chill("corona")

