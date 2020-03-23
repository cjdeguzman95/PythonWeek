# As a user I want to list all modules


class Modules:

    list_modules = ["Business Week", "SQL and AGILE", "Python Development", "Machine Learning", "Tableau"]

    def __init__(self, module_name, duration):
        self.module_name = module_name
        self.duration = duration

    def module_length(self):
        if self.module_name == "python development":
            print("This module is 2 weeks long")
        else:
            print("This module is a week long")

    def module_add(self):
        self.list_modules.append(self.module_name)

    def list_all(self):
        print(self.list_modules)


m = Modules("Final Project", 1)

m.module_add()
m.list_all()


# As a user I want to add a student to a batch
# As a user I want to list all students in a batch


class Batches:

    student_list = ["Weiyee", "CJ", "Gigi"]

    def __init__(self, module, start_date):
        self.module = module
        self.start_date = start_date

    def add_student(self, name):
        self.student_list.append(name)

    def list_all(self):
        print(self.student_list)


s1 = Batches("Python", "24th Feb")
s1.list_all()

s1.add_student("Tosin")
s1.list_all()


# As a user I want to create a Trainee


class Trainee:

    def __init__(self, name, age, id, stream):
        self.name = name
        self.age = age
        self.id = id
        self.stream = stream

    def info(self):
        print("Student details: {}, {} years old, ID {}, {}".format(self.name, self.age, self.id, self.stream))

    def trainer(self):
        if self.stream.lower() == "data":
            print("Isabella trains this student")
        else:
            print("Isabella doesn't train this student")


trainee1 = Trainee("CJ", 24, 1234, "Data")
trainee2 = Trainee("James", 22, 5678, "Devops")

trainee1.info()
trainee1.trainer()
