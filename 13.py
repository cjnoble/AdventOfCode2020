def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        #data = [[c for c in line] for line in data]

    return data

def check_busses (time, busses):
    while True:
        for bus in busses:
            if time%bus == 0:
                return time, bus

        time += 1


def mod(n, d):
    result = n%d
    if result ==0:
        return d
    else:
        return result

data = read_text_file("13.txt")

start_time = int(data[0])

busses = data[1]
busses = busses.split(",")

busses = [(time, int(buss)) for time, buss in enumerate(busses) if buss != "x"]
#buss_times = []

print(busses)

bus_multipes = [mod((bus[1] - bus[0]),bus[1]) for bus in busses]
print(bus_multipes)

m = 1
for multiple in bus_multipes:
    m *= multiple

print(m)
for bus in busses:
    print((m+bus[0], (m+bus[0])%bus[1]))

# t + i1 = A1*x1
# t + i2 = A2*x2
# t + i3 = A3*x3
# t + i4 = A4*x4