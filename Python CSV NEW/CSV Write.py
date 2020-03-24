import csv

with open("user_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("copy_user_data.csv", "w") as new_file:
        csv_write = csv.writer(new_file, delimiter=",")

        for line in csv_reader:
            csv_write.writerows(line)


# same but written differently
csv_file = open("user_data.csv", "r")
new_file = open("copy_user_data.csv", "w")

with csv_file:
    csv_reader = csv.reader(csv_file)

    with new_file:
        csv_writer = csv.writer(new_file, delimiter=",")

        for line in csv_reader:
            csv_writer.writerows(new_file)
