from gsa_tools.python_tools import read_text_file, value_gen
import re

file_name = "02.txt"

data = read_text_file(file_name)


def part_01 (data):

    valid = 0

    for row in data:
        pattern, password = row.split(":")
        #print(pattern)

        match = re.search("([0-9]+)-([0-9]+)", pattern)
        min_max = match.groups()
        min_n, max_n = (int(n) for n in min_max)
        
        match_letter = re.search("([a-z])", pattern)
        letter = match_letter.group(0)
        #print(letter)

        password_match = re.findall(letter, password)
        #print(password_match)

        if len(password_match) >= min_n and len(password_match) <= max_n:
            valid += 1

    print(valid)

def part_02 (data):

    valid = 0
    v_pass = []

    for row in data:
        pattern, password = row.split(": ")
        #print(pattern)

        match = re.search("([0-9]+)-([0-9]+)", pattern)
        min_max = match.groups()
        min_n, max_n = (int(n) for n in min_max)
        
        match_letter = re.search("([a-z])", pattern)
        letter = match_letter.group(0)
        #print(letter)

        #password_match = re.findall(letter, password)
        #print(password_match)

        #print (password[min_n - 1])
        #print (password[max_n - 1])

        if (password[min_n - 1] == letter) != (password[max_n - 1] == letter):
            valid += 1
            v_pass.append((password, letter, min_n, max_n))

    print(valid)
    #print(v_pass)

part_02(data)