


def read_data (file_name):

    with open(file_name, "r") as f:
        data = f.read()
        data = data.split("\n\n")

        data = [line.replace("\n", " ") for line in data]
        data = [line.split(" ") for line in data]

        #pprint_list(data)

    return data

file_name = "06.txt"

data = read_data(file_name)

total_length = 0
intersection_length = 0

for group in data:

    group_set = set()
    person_sets = []

    for person in group:
        person_set = set()

        for question in person:
            group_set.add(question)
            person_set.add(question)

        person_sets.append(person_set)

    intersection_set = person_sets[0]
    for person_set in person_sets:
        intersection_set = intersection_set.intersection(person_set)

    total_length += len(group_set)
    intersection_length += len(intersection_set)

print(total_length)
print(intersection_length)