




def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [line.split(" ") for line in data]

    return data


def contig_range (n):

    for i in range(n):
        for j in range(n):
            if j>i:
                yield i, j



def numbers (data, d, i):
    for n1 in range (i - d, i):
        n1 = data[n1]

        for n2 in range(i - d, i):
            n2 = data[n2]

            yield n1, n2


def test_number(data, d, i, n):

    for n1, n2 in numbers(data, d, i):
        x = n1 + n2
        if n1==n2:
            continue

        elif x == n:
            print(f"{n1} + {n2} = {n}")
            return True

    return False

data = read_text_file("09.txt")

data = [int(n[0]) for n in data]

d = 25

for i in range (d, len(data)):

    n = data[i]

    if test_number(data, d, i, n) is False:
        print(n)
        break

invalid_number = n
pos = i

data = data[:i]

for n1, n2 in contig_range(i):
    contig_data = data[n1:n2]

    if sum(contig_data) == invalid_number:
        print(min(contig_data) + max(contig_data))

