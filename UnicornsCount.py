import openpyxl as xl
from UnicornsCleaning import create_list, add_to_worksheet

path = "Unicorns_Dataset.xlsx"
wb = xl.load_workbook(path)
ws2 = wb["Investors"]
ws3 = wb["Counts"]


def count_freq(column):
    count = {investor: column.count(investor) for investor in column}
    return count


def get_investors(dic):
    investor = []
    for k in dic.keys():
        investor.append(k)
    return investor


def get_freq(dic):
    freq = []
    for v in dic.values():
        freq.append(v)
    return freq


# create iterable list for each column
col1 = create_list(ws2, 1)
col2 = create_list(ws2, 2)
col3 = create_list(ws2, 3)

# count frequency of each value in each column
c1 = count_freq(col1)
c2 = count_freq(col2)
c3 = count_freq(col3)

# extract keys/values from dictionary
first = get_investors(c3)
second = get_freq(c3)

# add and save to workbook
add_to_worksheet(first, ws3, 1, 5)
add_to_worksheet(second, ws3, 1, 6)
wb.save(path)
