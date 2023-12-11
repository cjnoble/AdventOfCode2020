from math import prod, gcd

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        #data = [[c for c in line] for line in data]

    return data


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


def part_1(card, door):

    card_loop = loop_size_trialanderror(card)
    door_loop = loop_size_trialanderror(door)
    print(f"Card loop: {card_loop}")
    print(f"Door loop: {door_loop}")

    encryption_key_card = do_loop(card_loop, door)
    encryption_key_door = do_loop(door_loop, card)

    print(f"Card encryption key: {encryption_key_card}")
    print(f"Door encryption key: {encryption_key_door}")

    return encryption_key_card 

def do_loop(loop_size, subject = 7):
    x = 1
    div = 20201227

    for i in range(loop_size):
        x *= subject
        x = x%div
    
    return x


def loop_size_trialanderror(key):
    mul = 7
    div = 20201227

    x = 1
    i = 0
    while True:
        x *= mul
        x = x%div
        i += 1

        if x == key:
            return i
    

def loop_size(key):
    return loop_size_trialanderror(key)
    # mul = 7
    # div = 20201227

    # return crt([mul, div], [key, key])


def part_2(data):

    return


if __name__ == "__main__":

    data = read_text_file("13.txt")

    print(part_1(10212254, 12577395))
    print(part_2(data))


