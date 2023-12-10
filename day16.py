import re
from functools import reduce


def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [row.split(",") for row in data]
        data = [[int(x) for x in row] for row in data]

    return data

def validate_field (n, field):
    '''
    returns true if n is a valid number for field
    ''' 
    for valid_range in field:
        if n >= valid_range[0] and n <= valid_range[1]:
            return True
    return False


def validate_all_fileds (n, fields):
    '''
    returns true if n is valid for any field
    '''
    for field in fields.values():
        if validate_field(n, field):
            return True

    return False


def get_valid_fields (n, fields):
    '''
    returns true if n is valid for any field
    '''
    valid_fields = []

    for key, field in fields.items():
        if validate_field(n, field):
            valid_fields.append(key)

    return valid_fields

def validate_tickett (row, fields):
    '''

    '''
    valid = True
    invalid_fields = []
    for n in row:
        if not validate_all_fileds(n, fields):
            invalid_fields.append(n)
            valid = False

    return valid, invalid_fields



your_ticket = [101,179,193,103,53,89,181,139,137,97,61,71,197,59,67,173,199,211,191,13]

fields = {
"departure location": " 49-920 or 932-950",
"departure station": " 28-106 or 130-969",
"departure platform": " 47-633 or 646-950",
"departure track": " 41-839 or 851-967",
"departure date": " 30-71 or 88-966",
"departure time": " 38-532 or 549-953",
"arrival location": " 38-326 or 341-968",
"arrival station": " 27-809 or 834-960",
"arrival platform": " 29-314 or 322-949",
"arrival track": " 26-358 or 368-966",
"class": " 34-647 or 667-951",
"duration": " 39-771 or 785-958",
"price": " 43-275 or 286-960",
"route": " 28-235 or 260-949",
"row": " 48-373 or 392-962",
"seat": " 35-147 or 172-953",
"train": " 37-861 or 885-961",
"type": " 38-473 or 483-961",
"wagon": " 49-221 or 228-973",
"zone": " 46-293 or 307-967"
}


for key, val in fields.items():
    match = re.findall("([0-9]+-[0-9]+)", val)
    valid = []
    for n in match:
        n = n.split("-")
        n = [int(i) for i in n]
        valid.append(n)
    fields[key] = valid


data = read_text_file("16.txt")

invalid = []

valid_data = []

for row in data:
    valid, invalid_fileds = validate_tickett(row, fields)
    invalid.extend(invalid_fileds)
    if valid:
        valid_data.append(row)

print(sum(invalid))

valid_field_list = []

for i in range (len(data[0])):
    all_valid = []
    for row in valid_data:
        field = row[i]

        valid_fields = get_valid_fields(field, fields)
        valid_fields = set(valid_fields)
        all_valid.append(valid_fields)


    all_valid = reduce(lambda s, x: s.intersection(x), all_valid)
    print(all_valid)
    valid_field_list.append(all_valid)


field_description = {}

unsolved = 1
while unsolved != 0:

    print(valid_field_list)
    remove = []
    unsolved = 0

    for i, row in enumerate(valid_field_list):
        if len(row) == 1:
            row = [r for r in row]
            field_description[i] = row[0]
            remove.append(row[0])
        else:
            unsolved += 1


    for field in fields.keys():
        test =  [field in row for row in valid_field_list]
        if sum(test) == 1:
            field_description[test.index(1)] = field
            valid_field_list[test.index(1)] = {field}
            #remove.append(field)

    for i, row in enumerate(valid_field_list):
        for removed_fields in remove:
            if removed_fields in row and len(row) > 1:
                row.remove(removed_fields)



print(valid_field_list)
print(field_description)

keys = []
for key, value in field_description.items():
    if "departure" in value:
        keys.append(key)

your_ticket = [your_ticket[i] for i in keys]

your_ticket = reduce(lambda a, b: a*b, your_ticket)
print(your_ticket)