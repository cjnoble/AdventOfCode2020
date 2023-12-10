from gsa_tools.python_tools import read_text_file, value_gen


file_name = "01.txt"

data = read_text_file(file_name)
data = [int(i) for i in data]

def part_1 (data):
    for number_1 in data:
        for number_2 in value_gen(data, number_1):
            if number_1 + number_2 == 2020:
                print(number_1 * number_2)

def part_2 (data):
    for number_1 in data:
        for number_2 in value_gen(data, number_1):
            for number_3 in value_gen (data, number_2):
                if number_1 + number_2 + number_3 == 2020:
                    print(number_1 * number_2 * number_3)

part_1(data)
part_2(data)