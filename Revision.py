# Inheritance

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        # Parent.__init__(self, fname, lname)
        super().__init__(fname, lname)  #super() is a shortcut to the init function above
        self.graduationyear = graduationyear

    def welcome(self):
        print("Welcome {} {} to the class of {}".format(self.fname, self.lname, self.graduationyear))



x = Person("Ivan", "De Guzman")
y = Student("CJ", "De Guzman", 2019)

x.printname()
y.welcome()



