from gsa_tools.python_tools import pprint_list, pprint_dict
import re

def read_data (file_name):

    with open(file_name, "r") as f:
        data = f.read()
        data = data.split("\n\n")

        data = [line.replace("\n", " ") for line in data]
        data = [line.split(" ") for line in data]

        pprint_list(data)

    return data

def build_dict (data):

    data_list = []

    for row in data:

        data_dict = {}

        for field in row:
            key, value = field.split(":")
            data_dict[key] = value

        data_list.append(data_dict)

    return data_list


def valid_number (value, min_valid, max_valid):
    try:
        value = int(value)
    except ValueError:
        return False

    if value < min_valid or value > max_valid:
        return False
    return True

def check_valid (row, required_keys):

    for key in required_keys:
        if key not in row:
            return False

        value = row[key]

        if key == "byr":
            if not valid_number (value, 1920, 2002):
                return False
            else:
                byr = value

        elif key == "iyr":
            if not valid_number (value, 2010, 2020):
                return False
            else:
                iyr = value

        elif key == "eyr":
            if not valid_number (value, 2020, 2030):
                return False
            else:
                eyr = value

        elif key == "hgt":
            match = re.match("([0-9]+)cm\Z", value)
            if match:
                height = float(match.group(1))
                if not valid_number (height, 150, 193):
                    return False
                else:
                    hgt = value
                    continue

            match = re.match("([0-9]+)in\Z", value)
            if match:
                height = float(match.group(1))
                if not valid_number (height, 59, 76):
                    return False
                else:
                    hgt = value
                    continue

            return False

        elif key == "hcl":
            match = re.match("#([0-9a-f]{6})\Z", value)
            if not match:
                return False
            else:
                hcl = value

        elif key == "ecl":
            valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value not in valid_colours:
                return False
            else:
                ecl = value

        elif key == "pid":
            match = re.match("([0-9]{9})\Z", value)
            if not match:
                return False
            else:
                pid = value

    valid_row = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    print(f"{valid_row} is valid")
    return True

data = read_data("04.txt")
data = build_dict(data)

pprint_list(data)

valid = 0

for row in data:

    if check_valid(row, [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
        ]):

        valid += 1

print(valid)