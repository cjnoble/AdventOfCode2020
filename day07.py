import re
from collections import defaultdict

def read_data (file_name):

    with open(file_name, "r") as f:
        data = f.read()
        data = data.split("\n")

        #data = [line.replace("\n", " ") for line in data]
        #data = [line.split(" ") for line in data]

        #pprint_list(data)

    return data


def parse_bag_string(bag_string):

    match = re.match("([0-9])", bag_string)
    if match:
        number = match.group(0)
        bag_string = bag_string.split(" ")
        colour = bag_string [1:3]
    else:
        number = 1
        bag_string = bag_string.split(" ")
        colour = bag_string [:2]

    colour = " ".join(colour)

    return number, colour


class Bag (object):
    def __init__ (self):
        self.name = ""
        self.contains = []
        self.is_contained_by = []
        self.contains_number = []

    def get_bags (self):
        
        if len(self.contains) > 0:

            bags = [[bag for i in range (int(n))] for bag, n in zip(self.contains, self.contains_number)]
            
            all_bags = []
            for bag in bags:
                all_bags.extend(bag)
            bags = all_bags

        else:
            bags = []

        return bags


data = read_data ("07.txt")
#print(data)

bags = defaultdict(Bag)

for rule in data:
    rule = re.split("contain |,", rule)

    bag = rule.pop(0)
    bag.strip()
    number, name = parse_bag_string(bag)
    bag_contain = bags[name]
    bag_contain.name = name

    for bag in rule:
        bag = bag.strip()
        bag.strip()
        number, name = parse_bag_string(bag)
        if name != "no other":
            bag_contain.contains.append(bags[name])
            bag_contain.contains_number.append(number)
            bags[name].is_contained_by.append(bag_contain)
        
    #print(rule)
    #break

valid = set()
gold_bag = bags["shiny gold"]

bags = gold_bag.is_contained_by

while True:
    if len(bags) == 0:
        break
    else:
        bag = bags.pop(0)
        valid.add(bag.name)

        if len(bag.is_contained_by) > 0:
            bags.extend(bag.is_contained_by)

print(valid)
print(len(valid))


bags = [gold_bag]
#bags ,gold_bag.contains.get_bags()
needed_bags = -1

while True:
    if len(bags) == 0:
        break
    else:
        bag = bags.pop(0)
        needed_bags += 1
        bags.extend(bag.get_bags())

print(needed_bags)