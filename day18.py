from operator import add, sub, mul, truediv

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = prep_data(data)

    return data

def prep_data(data):
    return [[c for c in line if c != " "] for line in data]

def calc_p (calc_string):
    #print(f"Calcing {calc_string}")

    operations_dict = {

        "+": add,
        "-": sub,
        "*" : mul,
        "/": truediv
    }

    if calc_string:
        cur_val = int(calc_string.pop(0))

        while calc_string:

            operator = operations_dict[calc_string.pop(0)]

            cur_val = operator(cur_val, int(calc_string.pop(0)))

        return cur_val
    return None

def calc_p1_ordering(calc_string):
    print(f"Eval: {calc_string}")
    #open_brackt = [a=="(" for a in calc_string]
    #close_bracket = [a==")" for a in calc_string]

    cur_string = []

    while len(calc_string) > 0:

        var = calc_string.pop(0)
        if var == "(":
            calc_string = (calc_p1_ordering(calc_string))
            #print(f"After applying brackets {cur_string}")

        elif var in ["+", "-", "*" ,"/"]:
            cur_string = [calc_p(cur_string)]
            cur_string.append(var)
            #return cal_val

        elif var == ")":
            cal_val = [calc_p(cur_string)]
            cal_val.extend(calc_string)
            return cal_val

        else:
            cur_string.append(var)

    return [calc_p(cur_string)]


def calc_p2_ordering(calc_string):
    print(f"Eval: {calc_string}")

    cur_string = []

    while len(calc_string) > 0:
        print(cur_string, calc_string)

        var = calc_string.pop(0)
        if var == "(":
            cur_string.extend(calc_p2_ordering(calc_string))
            calc_string = calc_p2_ordering(cur_string)

        elif var == "*" or var == "/":
            cur_string.append(var)
            calc_string  = calc_p2_ordering(calc_string)
            #cur_string = calc_p(cur_string)
            
        elif var == "+" or var == "-":
            cur_string = [calc_p(cur_string)]
            cur_string.append(var)
            #return cal_val

        elif var == ")":
            cal_val = [calc_p(cur_string)]
            cal_val.extend(calc_string)
            return cal_val

        else:
            cur_string.append(var)

    return [calc_p(cur_string)]


def part_1_verbose(data):

    for line in data:
        print(f"New Calc: {line}")
        print(f"Result {calc_p1_ordering(line)}")   


def part_1(data):

    results = [calc_p1_ordering(line)[0] for line in data] 
    
    return sum(results)

def part_2_verbose(data):

    for line in data:
        print(f"New Calc: {line}")
        print(f"Result {calc_p2_ordering(line)}")   


def part_2(data):

    results = [calc_p2_ordering(line)[0] for line in data] 
    
    return sum(results)

if __name__ == "__main__":

    print(part_1(read_text_file("18.txt")))
    part_2_verbose(read_text_file("18.txt"))
    print(part_2(read_text_file("18.txt")))

    # results = [brackets(line)[0] for line in data] 
    # print(sum(results))

    #print(calc(["8", "*", "3", "-", "2"]))