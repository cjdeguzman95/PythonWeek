# Exercises for 17/03/20


# Exercise 1: Sort the numbers from the original list into even and odd numbers and insert into new lists
list = [10, 111, 24, 56, 78, 75, 65, 80]

even_list = []
odd_list = []

for number in list:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print(even_list)
print(odd_list)


# Exercise 2: Giving the description for a film rating
film_rating = input("What is the film rating? ")

if film_rating == "universal":
    print("all age groups can watch this film")
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
else:
    print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")


# Exercise 3: Fizzbuzz
number = int(input("Give me a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("{} is a fizzbuzz number!".format(number))
elif number % 3 == 0:
    print("{} is a fizz number".format(number))
elif number % 5 == 0:
    print("{} is a buzz number!".format(number))
else:
    print("Unfortunately, {} is neither a fizz, buzz nor a fizzbuzz number!".format(number))


