from math import prod, gcd

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

# def gcd (a, b):
#     (old_r, r) = (a, b)
#     (old_s, s) = (1, 0)
#     (old_t, t) = (0, 1)

#     while r != 0:
#         quotient = old_r//r
#         (old_r, r) = (r, old_r − quotient × r)
#         (old_s, s) = (s, old_s − quotient × s)
#         (old_t, t) = (t, old_t − quotient × t)

#     return (old_s, old_d), old_r, (t, s)


def mul_inv(a, n):
    '''
    function inverse(a, n)
    t := 0;     newt := 1
    r := n;     newr := a

    while newr ≠ 0 do
        quotient := r div newr
        (t, newt) := (newt, t − quotient × newt) 
        (r, newr) := (newr, r − quotient × newr)

    if r > 1 then
        return "a is not invertible"
    if t < 0 then
        t := t + n

    return t'''

    n0 = n
    x0, x1 = 0, 1
    if n == 1: return 1
    while a > 1:
        q = a // n
        a, n = n, a%n
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += n0
    return x1


def co_prime(a, b):

    x, y = (a, b) if a>b else (b, a)

    return x%y != 0
    

def crt (n, a):
    '''
    Chinese remainder theorem
    n are the loops (modulo)
    a are the offsets (remainders)

    n must be pairwise coprime
    N is the product of n
    '''
    for n0, n1 in [(n0, n1) for n0 in n for n1 in n if n0!=n1] :
        if not co_prime(n0, n1):
            raise Exception(f"{n0} and {n1} are npt co prime")

    N = prod(n)
    s = 0

    for ni, ai in zip(n, a):
        y = N//ni
        #mi = mul_inv(y, ni)
        mi = pow(y, -1, ni) # mi*y = 1 (mod(ni))
        assert mi*y % ni == 1
        s += ai * mi * y

    return s % N


# def parse_input(data):

#     start_time = int(data[0])

#     print(f"Start Time {start_time}")

#     busses = parse_busses(data[1])

#     print(f"Buss Data {busses}")

#     return start_time, busses

def parse_start_time(row):
    start_time = int(row)

    print(f"Start Time {start_time}")
    return start_time

def parse_busses(row):
    row = row.split(",")
    buss_data = [(time, int(buss)) for time, buss in enumerate(row) if buss != "x"]
    return buss_data

def part_1(data):

    start_time = parse_start_time(data[0])
    busses = parse_busses(data[1])

    busses_loops = [buss[1] for buss in busses]

    ID, wait = min([(loop, loop - start_time%loop) for loop in busses_loops], key =lambda x: x[1])

    return ID * wait


def part_2(data):

    return solve_busses(data[1])


def solve_busses(busses):
    busses = parse_busses(busses)
    buss_offsets = [buss[0] for buss in busses]
    buss_loop_times = [buss[1] for buss in busses]
    buss_remainders = [(loop - offset)%loop for loop, offset in zip(buss_loop_times, buss_offsets)]

    print(f"Buss loop times {buss_loop_times }")
    print(f"Buss offsets {buss_offsets}")
    print(f"Buss remainders {buss_remainders}")

    time = crt(buss_loop_times, buss_remainders)

    for bus, offset in zip(buss_loop_times, buss_remainders):
        print(f"For bus {bus}, expected remainder is {offset}, actual remainder is {time%bus}")

    return time

if __name__ == "__main__":

    data = read_text_file("13.txt")

    print(part_1(data))
    print(part_2(data))


