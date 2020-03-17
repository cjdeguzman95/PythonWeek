# Exercises for 17/03/20

# Exercise 1: sort the numbers in the original list into even and odd numbers - insert into new lists
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

