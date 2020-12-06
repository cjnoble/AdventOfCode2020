from math import ceil, floor
import re


def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [line.split(" ") for line in data]

    return data


def binary_search (search_list, top=True):

    mid = len(search_list)/2

    if top:
        mid = floor(mid)
        return search_list[:mid]

    else:
        mid = ceil(mid)
        return search_list[mid:]


def seat_match (seat_string):

    match = re.search("([FB]+)([LR]+)" , seat_string)

    row, col = match.groups(0)

    #print(row)
    #print(col)

    row = [s for s in row]
    col = [s for s in col]

    row_max = 128
    col_max = 8

    rows = [i for i in range(row_max)]
    cols = [i for i in range(col_max)]

    while row:
        rows = binary_search(rows, row.pop(0) == "F")
    row = rows[0]

    while col:
        cols = binary_search(cols, col.pop(0) == "L")
    col = cols[0]

    ID = row * 8 + col

    #print(row)
    #print(col)
    #print(ID)

    return row, col, ID


file_name = "05.txt"

data = read_text_file(file_name)
#print(data)

ID_max = 0

seat_set = set()
ID_set = set()

for seat in data:
    row, col, ID = seat_match(seat[0])
    ID_max = max(ID, ID_max)

    seat_set.add ((row, col))
    ID_set.add(ID)


row_max = 128
col_max = 8

missing_row = []
missing_column = []
missing_ID = []

for row in range (row_max):

    for col in range(col_max):

        #print(row)
        #print(col)

        if (row, col) not in seat_set:

            print(row)
            missing_row.append(row)
            missing_column.append(col)
            missing_ID.append(row*8+col)

print(missing_ID)

for i in range(1, len(missing_ID) - 1):

    if missing_ID[i-1] + 1 == missing_ID[i] or missing_ID[i+1] - 1 == missing_ID[i]:
        pass
    else:
        print(missing_ID[i])

