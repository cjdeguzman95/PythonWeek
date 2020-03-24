import openpyxl as xl

# store the file path in a variable
path = "Practice2.xlsx"

# to work an existing workbook
workbook = xl.load_workbook(path)
sheet = workbook["Task"]

followers = [
    ("Number", "Social Media", "Follower Count"),
    (1, "Facebook", "1790"),
    (2, "Instagram", "780")
]

for i in followers:
    sheet.append(i)

workbook.save(path)

