TARGET = 20
MAX_GUESS = 5

name = str(input("What is your name? "))

print("Let's play a game {}\nI'm thinking of a number between 1 and 100.\nCan you guess what it is?".format(name.capitalize()))
print("You have {} guesses".format(MAX_GUESS))

while MAX_GUESS != 0:
    try:
        guess = int(input("What number am I thinking of? "))
    except ValueError as err:
        print("Please insert numeric characters {}".format(name.capitalize()))
    else:
        if guess != TARGET:
            MAX_GUESS -= 1
            if guess < 1 or guess > 100:
                print("I mean... that's out of range {}!".format(name.upper()))
            elif guess > 20:
                print("It's smaller than that!")
            else:
                print("Try a bigger number")
            print("You have {} guesses left".format(MAX_GUESS))
        else:
            print("That's correct! You won!")
            break
else:
    print("Sorry, you're out of guesses! Better luck next time!")

