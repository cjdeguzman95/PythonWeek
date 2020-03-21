# class, inheritance and abstraction revision

# Practice 1


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        # Parent.__init__(self, fname, lname)
        super().__init__(fname, lname)                #super() is a shortcut to the init function above
        self.graduationyear = graduationyear

    def welcome(self):
        print("Welcome {} {} to the class of {}".format(self.fname, self.lname, self.graduationyear))



x = Person("Ivan", "De Guzman")
y = Student("CJ", "De Guzman", 2019)

x.printname()
y.welcome()

# Practice 2

class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def eat(self):
        print("{} says I am eating chicken!".format(self.name).capitalize())


Animal1 = Animal("dog", "bella", 12)
Animal2 = Animal("cat", "mimi", 6)
