def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [[c for c in line] for line in data]

    return data

class Seat(object):

    def __init__ (self, coordinates):
        self.occupied = False
        self.adjacent = []
        self.coordinates = coordinates

data = read_text_file("11.txt")

seats_dict = {}

for row in range(len(data)):
    for column in range(len(data[row])):

        test = data[row]
        test_2 = data[row][column]
        test_3 = data[row][column][0]

        pos = data[row][column]
        if pos == "L":
            seat = Seat((row, column))
            seats_dict[(row, column)] = seat

            # for adjacent in [(row - 1, column), (row, column - 1), (row - 1, column - 1), (row - 1, column + 1)]:
            #     if adjacent in seats_dict.keys():
            #         adjacent_seat = seats_dict[adjacent]
            #         adjacent_seat.adjacent.append(seat)
            #         seat.adjacent.append(adjacent_seat)

            for direction in [(-1, 0), (0, -1), (-1, -1), (-1, +1)]:
                row_i = row
                column_i = column
                while True:
                    row_i += direction[0]
                    column_i += direction[1]

                    if row_i < 0 or column_i < 0:
                        break

                    if (row_i, column_i) in seats_dict.keys():
                        adjacent_seat = seats_dict[(row_i, column_i)]
                        adjacent_seat.adjacent.append(seat)
                        seat.adjacent.append(adjacent_seat)               
                        break

iteration = 0

while True:

    changed_seats = 0
    print("New iteration")

    for seat in seats_dict.values():
        seat.adjacency_occupation = [s.occupied for s in seat.adjacent]

    for seat in seats_dict.values():

        if sum(seat.adjacency_occupation) == 0 and not seat.occupied:
            changed_seats =+ 1
            seat.occupied = True

        elif sum(seat.adjacency_occupation) >= 5 and seat.occupied:
            changed_seats =+ 1
            seat.occupied = False


    data_plot = [["." for col in range(len(data[row]))] for row in range(len(data))]

    for seat in seats_dict.values():
        
        row, column = seat.coordinates
        data_plot[row][column] = "#" if seat.occupied else "L"

    for row in data_plot:
        row = "".join(row)
        print(row)

    #input()

    if changed_seats == 0:
        break

        
occupied = len([seat for seat in seats_dict.values() if seat.occupied])
print(occupied)