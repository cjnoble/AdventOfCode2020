

test_data = [0,3,6]
data = [0,13,1,8,6,15]

seen = {}
last_seen = 0

for i in range (30000000):

    if data:
        n = data.pop(0)

    else:
        if last_seen in seen.keys():
            n = i - seen[last_seen] - 1
        else:
            n = 0
        
    #print((i, n))

    if i != 0:
        seen[last_seen] = i - 1
        last_seen = n

print(n)