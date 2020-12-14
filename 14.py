import re

def read_text_file (file_name):

    with open(file_name, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

    return data


def part_01 (data):
    for row in data:
        if "mask" in row:
            match = re.search("([0-1X]+)", row)
            mask = match.group()
            print(mask)
        else:
            match = re.findall("([0-9]+)", row)
            mem = int(match[0])
            value = int(match[1])
            bin_val = format(value, 'b')
            str_val = "0"*(len(mask) - len(bin_val)) + bin_val

            str_val = [s for s in str_val]

            print(mem)
            print(value)
            print(bin_val)
            print(str_val)

            for m, s in zip(mask, enumerate(str_val)):
                if m != "X":
                    str_val[s[0]] = m
                    

            bin_val = "".join(str_val)
            value = int(bin_val, 2)
            mem_dict[mem] = value
    return mem_dict

def list_replace (l, pos_list):
    if len(pos_list) == 0:
        return l

    else:
        pos = pos_list.pop(0)
        old_l = l.copy()
        for l1 in old_l:
            l2 = l1.copy()
            l.append(l2)
            l1[pos] = "0"
            l2[pos] = "1"

        list_replace(l, pos_list)

    return l



data = read_text_file("14.txt")

mem_dict = {}

for row in data:
    if "mask" in row:
        match = re.search("([0-1X]+)", row)
        mask = match.group()

        match = re.finditer("X", mask)
        x_match = [x.span()[0] for x in match]

        mask_or = mask.replace("X", "0")
        mask_or = int(mask_or, 2)

        #print (x_match)

        #print(mask)
    else:
        match = re.findall("([0-9]+)", row)
        mem = int(match[0])
        value = int(match[1])

        mem = mem | mask_or

        mem_bin = format(mem, 'b')
        mem_bin = "0"*(len(mask) - len(mem_bin)) + mem_bin

        mem_list = [s for s in mem_bin]
        mem_list = list_replace([mem_list], x_match.copy())

        for mem in mem_list:
            mem = "".join(mem)
            #print(mem)
            mem = int(mem, 2)
            #print(mem)
            mem_dict[mem] = value

        # bin_val = format(value, 'b')
        

        # 

        # print(mem)
        # print(value)
        # print(bin_val)
        # print(str_val)

        # for m, s in zip(mask, enumerate(str_val)):
        #     if m != "X":
        #         str_val[s[0]] = m
                

        # bin_val = "".join(str_val)
        # value = int(bin_val, 2)
        # mem_dict[mem] = value

print(sum(mem_dict.values()))