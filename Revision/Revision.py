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


# Practice 2


class Spartan:
    def __init__(self, name, course, week):
        self.name = name
        self.course = course
        self.week = week

    def greeting(self):
        return "Hi, my name is {}".format(self.name)

    def stream(self):
        return "{} is on the {} stream".format(self.name, self.course)

    def trainer(self):
        if self.course == "data":
            return "Isabella trains {}".format(self.name)
        else:
            return "Isabella does not train {}".format(self.name)

    def IsTraining(self):
        if self.week <= 10:
            return "{} is still training".format(self.name)
        else:
            return "{} has graduated from Sparta Academy".format(self.name)


x = Spartan("CJ", "data", 5)
y = Spartan("Mike", "devops", 13)

print(y.trainer(), ". Also,", y.IsTraining())
print("{} and {}.".format(x.stream(), x.IsTraining()))
