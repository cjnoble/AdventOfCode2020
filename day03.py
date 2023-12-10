from gsa_tools.python_tools import read_text_file, value_gen
import re

file_name = "03.txt"

data = read_text_file(file_name)


def trees (data, right, down):


    # right = 3
    #down = 1

    x = 0
    z = 0

    n_trees = 0

    row_length = len(data[0])

    while z < len(data):

        test = data[z][x]
        #print(test)

        if test == "#":
            n_trees += 1

        x += right
        x = x % row_length

        z += down

    #print(tress)

    return n_trees


tree_data = [trees(data, i, 1) for i in range (1, 9, 2)] 

tree_data.append(trees(data, 1, 2))


print(tree_data)

product = 1
for tree in tree_data:
    product *= tree

print(product)