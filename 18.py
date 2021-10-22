from operator import add, sub, mul, truediv

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [[c for c in line if c != " "] for line in data]

    return data


def calc (calc_string):

    operations_dict = {

        "+": add,
        "-": sub,
        "*" : mul,
        "/": truediv
    }

    cur_val = int(calc_string.pop(0))

    while calc_string:


        operator = operations_dict[calc_string.pop(0)]

        cur_val = operator(cur_val, int(calc_string.pop(0)))


    return cur_val


def brackets(calc_string):

    #open_bracket = [a=="(" for a in calc_string]
    #close_bracket = [a==")" for a in calc_string]

    cur_string = []

    while len(calc_string) > 0:

        var = calc_string.pop(0)
        if var == "(":
            cur_string.extend(brackets(calc_string))

        elif var == "*" or var == "/":
            cur_string.extend(brackets(calc_string))
            cur_string.append(var)

        elif var == "+" or "-":
            cal_val = [calc(cur_string)]
            cur_string.append(var)
            return cal_val

        elif var == ")":
            cal_val = [calc(cur_string)]
            #cal_val.extend(calc_string)
            return cal_val

        else:
            cur_string.append(var)

    return [calc(cur_string)]

data = read_text_file("18.txt")

for line in data:
    print(line)
    print(brackets(line))

# results = [brackets(line)[0] for line in data] 
# print(sum(results))

#print(calc(["8", "*", "3", "-", "2"]))