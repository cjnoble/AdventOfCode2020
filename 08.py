

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [line.split(" ") for line in data]

    return data


def acc (arg):
    global accumulator
    accumulator += arg
    global instruction_counter
    instruction_counter += 1
    return

def jmp(arg):
    global instruction_counter
    instruction_counter += arg

def nop(arg):
    global instruction_counter
    instruction_counter += 1


operation_dict = {
    "nop": nop,
    "jmp": jmp,
    "acc": acc
}

data = read_text_file("08.txt")
#print(data)

def run (data):
    global accumulator
    accumulator = 0
    global instruction_counter
    instruction_counter = 0
    instruction_set = set()

    while True:

        if instruction_counter in instruction_set:
            print("Loop")
            print(accumulator)
            return "Loop"
        instruction_set.add(instruction_counter)

        try:
            operation, argument = data[instruction_counter]
        except IndexError:
            print("End")
            print(accumulator)
            return "End"

        argument = int(argument)

        operation = operation_dict[operation]

        operation(argument)

for instruction in data:

    if instruction[0] == "jmp":
        instruction[0] = "nop"

    elif instruction[0] == "nop":
        instruction[0] = "jmp"

    response = run(data)
    if response == "End":
        break

    if instruction[0] == "jmp":
        instruction[0] = "nop"

    elif instruction[0] == "nop":
        instruction[0] = "jmp"