class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

    def age(self):
        print("I am " + self.age)


p1 = Person("John", 36)

p1.myfunc()
p1.age()
