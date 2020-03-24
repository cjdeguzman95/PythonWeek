# create an excel file called Data 9 with all trainee names
import xlsxwriter as xw

workbook = xw.Workbook("Data 9.xlsx")
worksheet = workbook.add_worksheet("Trainees")

worksheet.write("A1", "Trainee Name")

trainees = ["CJ", "Weiyee", "Gigi", "Shugs", "Andy", "Jonny", "Sassy", "Khanhi",
           "Ben", "Vivek", "Vijay", "Tosin", "Yin"]

row = 3
column = 0

for name in trainees:
    worksheet.write(row, column, name)
    row += 1

workbook.close()

# debugging - check what information will be included in the file
print(row)
print(column)
print(trainees)
