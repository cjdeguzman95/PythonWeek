import csv

# create a function that chooses only first names and emails from csv file


def transform_data(user_data):
    new_user_data = []

    with open("user_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            transformation = []
            transformation.append(line[0])
            transformation.append(line[2])
            new_user_data.append(transformation)

    return new_user_data


# create a function that copies new dataset into a new csv file


def create_new_file(new_file_name="new user data 2.csv"):
    new_user_data = transform_data(create_new_file)
    new_file = open(new_file_name, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_file()
