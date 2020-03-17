# Exercises for 16/03/20
import time

# Exercise 1: Extract details from the user
full_name = input("What is your full name? ")
birth_year = int(input("What year were you born in? "))
age = 2020 - birth_year
address = int(input("What is the first line of your address? "))
postcode = input("What is your postcode? ")

print("Hi {}, I know that you are {} years old and you live in {}, {}".format(full_name, age, address, postcode))


# Exercise 2: Check if a word is a palindrome
word = input("Give me a word: ")
word_reversed = word[::-1]

print("Is this word a palindrome?")
time.sleep(2)

if word_reversed == word:
    print("Wow, {} is a palindrome!".format(word))
else:
    print("Unfortunately, {} is not a palindrome!".format(word))


# Exercise 3: check if a number is odd or even
number = int(input("Give me a number: "))

print("Is this number odd or even?")
time.sleep(2)

if number % 2 == 0:
    print("{} is an even number!".format(number))
else:
    print("{} is an odd number!".format(number))


# Exercise 4: Check which number is the largest
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))
num3 = int(input("Give me a third and final number: "))

print("Which number is the largest?")
time.sleep(2)

if num1 > num2 and num1 > num3:
    print("the first number, {}, is the largest!".format(num1).capitalize())
elif num2 > num1 and num2 > num3:
    print("the second number, {}, is the largest!".format(num2).capitalize())
else:
    print("the third number, {}, is the largest!".format(num3).capitalize())
