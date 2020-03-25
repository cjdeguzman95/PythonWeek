import csv

with open("user_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        print(line)


# same but written differently
csv_file = open("user_data.csv", "r")
with csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

