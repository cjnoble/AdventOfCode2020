import re
from math import sin, cos, radians


class Boat (object):
    def __init__(self, position = [0,0], orientation = 90):
        self.position = position
        self.orientation = orientation

    def R (self, angle):
        self.orientation += angle

    def L (self, angle):
        self.R(-angle)

    def F (self, amount):
        self.position[0] += amount*sin(radians(self.orientation))
        self.position[1] += amount*cos(radians(self.orientation))

    def N (self, amount):
        self.position[1] += amount

    def S(self, amount):
        self.N(-amount)

    def E(self, amount):
        self.position[0] += amount

    def W(self, amount):
        self.E(-amount)


class Waypoint (object):
    def __init__(self, position = [1,10]):
        self.position = position
        #self.orientation = orientation

    def R (self, angle):
        self.orientation += angle

    def L (self, angle):
        self.position[0] += sin(radians(self.orientation))
        self.position[1] += cos(radians(self.orientation))

    def F (self, amount):
        self.position[0] += amount*sin(radians(self.orientation))
        self.position[1] += amount*cos(radians(self.orientation))

    def N (self, amount):
        self.position[1] += amount

    def S(self, amount):
        self.N(-amount)

    def E(self, amount):
        self.position[0] += amount

    def W(self, amount):
        self.E(-amount)


def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        #data = [[c for c in line] for line in data]

    return data



data = read_text_file("12.txt")
print(data)

ferry = Boat()

ferry_instructions = {
    "F": ferry.F,
    "L": ferry.L,
    "R": ferry.R,
    "N": ferry.N,
    "E": ferry.E,
    "W": ferry.W,
    "S": ferry.S
}

for row in data:
    #print(row)
    match = re.match("([A-Z]+)([0-9]+)", row)
    direction, amount = match.groups()
    #print(match.groups())
    amount = int(amount)

    instruction = ferry_instructions[direction]
    instruction(amount)

print(ferry.position)




