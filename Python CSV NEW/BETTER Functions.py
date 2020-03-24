# create a function that chooses chooses the first and last names from csv file
import csv


def transform_data():
    new_user_data = []

    with open("user_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            transformation = []
            transformation.append(line[0])
            transformation.append(line[1])
            new_user_data.append(transformation)

    return new_user_data


def create_new_file():
    new_user_data = transform_data()

    with open("full name.csv", "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_file()
