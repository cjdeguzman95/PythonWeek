import xlsxwriter as xw

workbook = xw.Workbook("Practice.xlsx")
ws1 = workbook.add_worksheet(name="Hello")
ws2 = workbook.add_worksheet()

ws1.write("A1", "Hello World")
ws1.write(1, 0, "Goodbye")

workbook.close()

