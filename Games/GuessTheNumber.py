'''
A game that lets the user guess which number the programme is thinking.
To help the user, the programme provides a hint and keeps track of their guess count!
Also uses Try/Except block to make sure user only inputs numbers.
'''

import time
from random import randrange

MAX_GUESS = 5
target_number = randrange(21)


print("Let's play a game...")
time.sleep(1)

name = str(input("What is your name? "))

print("I'm thinking of a number between 1 and 20")
time.sleep(1)

print("{}, can you guess what it is?".format(name.capitalize()))
time.sleep(1)

print("You have {} guesses!".format(MAX_GUESS))
time.sleep(1)

if target_number % 2 == 0:
    print("It's an even number!")
elif target_number % 2 != 0:
    print("It's an odd number!")

while MAX_GUESS != 0:
    try:
        guess = int(input("What number am I thinking of? "))
    except ValueError as err:
        print("Please insert numeric characters {}".format(name.capitalize()))
    else:
        if guess != target_number:
            MAX_GUESS -= 1
            if guess < 1 or guess > 20:
                print("I mean... that's out of range {}!".format(name.upper()))
            else:
                print("Wrong number {}! Try Again!".format(name.capitalize()))
                print("You have {} guesses left".format(MAX_GUESS))
        else:
            print("That's correct! You won!")
            break
else:
    print("Sorry {}, you're out of guesses! Better luck next time!".format(name.capitalize()))
    print("I was thinking of {}".format(target_number))