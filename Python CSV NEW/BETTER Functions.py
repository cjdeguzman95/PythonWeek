# create a function that chooses the first and last names from csv file
import csv


def transform_data(file_name):
    new_user_data = []

    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            transformation = []
            transformation.append(line[0])
            transformation.append(line[1])
            new_user_data.append(transformation)

    return new_user_data


def create_new_file(file_name, new_file_name):
    new_user_data = transform_data(file_name)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_file()
