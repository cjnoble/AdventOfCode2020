import re
from math import sin, cos, radians, tan, atan2, degrees, pi


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

    def F_waypoint(self, waypoint, amount):
        waypint_pos = waypoint.position
        self.position = [p + wp*amount for p, wp in zip(self.position, waypint_pos) ]


class Waypoint (object):
    def __init__(self, position = [10,1]):
        self.set_position(position)
        #self.orientation = orientation

    def set_position (self, position):
        self.position = position
        self.orientation = degrees(atan2(position[1], position[0]))

    def update_position (self):
        l = sum([p**2 for p in self.position])**0.5
        
        x = 1 if self.orientation < pi else -1
        y = x*tan(radians(self.orientation))
        unit_l = (x**2 + y**2)**0.5

        x = l*x/unit_l
        y = l*y/unit_l
        self.position = [x, y]

    def R (self, angle):
        self.orientation += angle
        self.update_position()

    def L (self, angle):
        self.R(-angle)

    # def F (self, amount):
    #     self.position[0] += amount*sin(radians(self.orientation))
    #     self.position[1] += amount*cos(radians(self.orientation))

    def N (self, amount):
        self.position[1] += amount
        self.set_position(self.position)

    def S(self, amount):
        self.N(-amount)

    def E(self, amount):
        self.position[0] += amount
        self.set_position(self.position)

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
waypoint = Waypoint()

ferry_instructions = {
    "F": ferry.F_waypoint,
    "L": waypoint.L,
    "R": waypoint.R,
    "N": waypoint.N,
    "E": waypoint.E,
    "W": waypoint.W,
    "S": waypoint.S
}

for row in data:
    #print(row)
    match = re.match("([A-Z]+)([0-9]+)", row)
    direction, amount = match.groups()
    #print(match.groups())
    amount = int(amount)

    instruction = ferry_instructions[direction]
    if instruction != ferry.F_waypoint:
        instruction(amount)
    else:
        instruction(waypoint, amount)

    print(ferry.position)
    print(waypoint.position)

print(ferry.position)
print(round(abs(ferry.position[0]) + abs(ferry.position[1]), 0))




