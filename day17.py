from collections import defaultdict



class Cube (object):
    def __init__ (self):
        #self.coordinates = None
        self.active = False
        self.change = False


def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [[c for c in line] for line in data]

    return data

def update (x, max_list, min_list, i):

    if x > max_list[i]:
        max_list[i] = x
    elif x < min_list[i]:
        min_list[i] = x

    return

def adjacent_coords (coords):
    adjacent = []
    for i in range (3):
        for j in range (3):
            for k in range (3):
                for h in range (3): 
                    new_coord = tuple(coord - 1 + x for coord, x in zip(coords, [i, j, k, h]))
                    if new_coord != coords:
                        adjacent.append(new_coord)
    return adjacent

data = read_text_file("17.txt")


cubes = defaultdict (Cube)

z = 0
w = 0
min_list = [0 for i in range(4)]
max_list = [0 for i in range(4)]


for row_i, row in enumerate(data):
    update(row_i, max_list, min_list, 1)
    
    for column_i, cube in enumerate(row):

        update(column_i, max_list, min_list, 0)

        if cube == "#":
            cubes[(column_i, row_i, z, w)].active = True


plot = [[[["." for i in range(min_list[0] - 1, max_list[0] + 2)] for i in range(min_list[1] - 1, max_list[1] + 2)] for i in range(min_list[2] - 1, max_list[2] + 2)] for i in range(min_list[3] - 1, max_list[3] + 2)]
for key, cube in cubes.items():
    if cube.active:
        x, y, z, w = key
        plot[w - min_list[3] + 1][z - min_list[2] + 1][y - min_list[1] + 1][x - min_list[0] + 1] = "#"

for w in plot:
    for z in w:
        for row in z:
            print(row)
        print("~")
print ("  =============  ")
iteration = 0
while iteration < 6:

    min_list_iter = min_list.copy()
    max_list_iter = max_list.copy()


    for x in range(min_list_iter[0] - 1, max_list_iter[0] + 2):
        for y in range(min_list_iter[1] - 1, max_list_iter[1] + 2):
            for z in range(min_list_iter[2] - 1, max_list_iter[2] + 2):
                for w in range(min_list_iter[3] - 1, max_list_iter[3] + 2):
                    coords = (x, y, z, w)
                    if coords == (3, 1, 0, 0):
                        print (coords)

                    cube = cubes[coords]

                    adjacent = adjacent_coords(coords)
                    adjacent = [cubes[coord].active for coord in adjacent]
                    adjacent = sum(adjacent)

                    if cube.active:
                        if adjacent < 2 or adjacent > 3:
                            cube.change = True

                    else:
                        if adjacent == 3:
                            cube.change = True
                            update(x, max_list, min_list, 0)
                            update(y, max_list, min_list, 1)
                            update(z, max_list, min_list, 2)
                            update(w, max_list, min_list, 3)
    
    plot = [[[["." for i in range(min_list[0] - 1, max_list[0] + 2)] for i in range(min_list[1] - 1, max_list[1] + 2)] for i in range(min_list[2] - 1, max_list[2] + 2)] for i in range(min_list[3] - 1, max_list[3] + 2)]
    for key, cube in cubes.items():
        if cube.change:
            cube.active = not cube.active
            cube.change = False
        if cube.active:
            x, y, z, w = key
            plot[w - min_list[3] + 1][z - min_list[2] + 1][y - min_list[1] + 1][x - min_list[0] + 1] = "#"

    # for z in plot:
    #     for row in z:
    #         print("".join(row))
    #     print("~")
    # print ("  =============  ")

    iteration += 1

active_cubes = 0
for cube in cubes.values():
    if cube.active:
        active_cubes +=1

print(active_cubes)