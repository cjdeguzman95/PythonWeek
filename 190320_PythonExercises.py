# # Exercises for 19/03/20
#
# # Exercise 1: Define mathematical functions
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# print(add(2, 6))
# print(subtract(2, 6))
# print(multiply(2, 6))
# print(divide(2, 6))
#
# # Exercise 2: Create a class called 'Car'
#
#
# class Car:
#
#     car_brand = "Toyota"
#
#     def sound(self):
#         return "Vroom"
#
#
# print(Car.car_brand)
# print(type(Car))
#
# # Exercise 3: Create a class called 'Fizzbuzz'
#
#
# class Fizzbuzz:
#     def __init__(self, number):
#         self.number = number
#
#     def isFizzbuzz(self):
#         if self.number % 3 == 0 and self.number % 5 ==0:
#             print("Fizzbuzz")
#         elif self.number % 3 == 0:
#             print("Fizz")
#         elif self.number % 5 == 0:
#             print("Buzz")
#         else:
#             print(self.number)
#
#
# number_range = range(101)
# for n in number_range:
#     num1 = Fizzbuzz(n)
#     num1.isFizzbuzz()

# Exercise 4: Create a class called 'Student'


class Student:

    def __init__(self, name, age, homeless):
        self.name = name
        self.age = age
        self.homeless = homeless

    def student_age(self):
        print("{} is {} years old".format(self.name, self.age))

    def need_stay(self):
        if self.homeless is True:
            print("{} needs housing".format(self.name))
        else:
            print("doesn't need housing")


student1 = Student('James', 19, False)
student2 = Student('Sarah', 23, True)

student1.student_age()
student2.need_stay()