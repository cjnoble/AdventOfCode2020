from itertools import tee
from python_tools import value_gen

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [line.split(" ") for line in data]

    return data

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

data = read_text_file("10.txt")

data = [int(n[0]) for n in data]
data.append(0)

sorted_data = sorted(data)
print(sorted_data)
sorted_data.append(sorted_data[-1] + 3)

diff = [0, 0, 0, 0]

for a, b in pairwise(sorted_data):
    print((a, b))
    if b - a < 4:
        diff[b - a] += 1

print(diff[1] * diff[3])

known_connections = {}

def number_of_connections (sorted_data, n, seq):
    connections = -1
    for m in value_gen(sorted_data, n):
        if m - n < 4:
            global known_connections
            connections += 1
            seq.append(m)
            if m in known_connections.keys():
                connections += known_connections[m]
            else:
                known_connections[m] = number_of_connections(sorted_data, m, seq)
                connections += known_connections[m]
    
    if connections == -1:
        connections = 0

    return connections


print(number_of_connections(sorted_data, 0, [0]) + 1)

print(known_connections)
    