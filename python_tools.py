from itertools import tee
from string import whitespace
from csv import DictWriter, DictReader
from os import listdir, path
import subprocess
from functools import reduce

class default_number (object):
    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True


def pprint_dict(dic):
    '''
    pretty print for dictionary
    '''
    print("{")
    for key, value in dic.items():
        if isinstance(value, list):
            print( f"{key}:")
            pprint_list(value)
        else:
            print(f"{key}: {value}")
    print("}")

def pprint_list(l):
    '''
    pretty print for lists
    '''
    print("[")
    for item in l:
        print(item)
    print("]")


def value_gen(all_values, target):
    '''
    Retuns an iterator of all items after the target item
    '''

    i = all_values.index(target)
    for j in range(i+1, len(all_values)):
        yield all_values[j]

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def read_text_file (file_name, split=None):
    '''
    Reads in a text file and returns a list of lines
    If split is specified, this char will be used as a split charachter on the lines
    In this case a list of lists is returned
    '''


    with open(file_name, "r") as f:
        data = f.readlines()

        output = [line.replace("\n","") for line in data]

        if split:
            if split == whitespace:
                output = [o.split() for o in output]
            else:
                output = [o.split(split) for o in output]

    return output


def data_str(s):

    if s == None:
        return ""

    else:
        return str(s)


def data_row (data, sep_char = ","):

    if reduce(lambda x, y: x and y, [isinstance(d, str) or d is None for d in data]):
        # List of strings (have to check this first, as it will look like a list of lists)
        data = [data_str(s) for s in data]
        return sep_char.join(data)

    try:
        # List of Lists
        return "\n".join([sep_char.join([data_str(d) for d in row]) for row in data])

    except TypeError:
        # Simple List
        return sep_char.join([data_str(d) for d in data])
        
    except Exception as e:
        raise e


def write_text_file (file_name, data):
    '''
    Wrties a text file
    data can be either a string or iterable
    '''

    with open(file_name, "w") as f:

        if isinstance(data, str):
            f.write(data)
        else:
            data = "\n".join(data)
            f.write(data)

    return


def write_csv_file (file_name, data:dict):
    '''
    Writes a csv file
    '''
    try:
        with open(file_name, "w", newline="") as f:

            writer = DictWriter(f, data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    except PermissionError:
        folder, file_name = path.split(file_name)
        file_name, extension = path.splitext(file_name)

        file_name = path.join(folder, f"{file_name}_1{extension}")

        write_csv_file(file_name, data)

    return

def read_csv_file (file_name):
    '''
    Reads a csv file
    '''

    with open(file_name, "r") as f:

        reader = DictReader(f)
        print(reader)

    return reader

def write_row_dict(file_name, row_dict):

    with open(file_name, 'w') as f:
        for key, data in row_dict.items():
            elem = str(key)
            data = [str(d) for d in data]
            res_row = ",".join(data)
            elem += "," + res_row
            elem  += "\n"
            f.write(elem)

def multi_file(folder_path, extension):
    '''
    returns file_paths, file_names as lists
    '''

    if extension[0] != ".":
        extension = "." + extension

    n = len(extension)

    files = listdir(folder_path)
    file_paths = list()
    file_names = []
    for f in files:
        if f[-n:] == extension:
            file_paths.append(path.join(folder_path,f))
            file_names.append(f)
    
    return file_paths, file_names


def list_filelinks (folder_ref):

    files = listdir(folder_ref)

    for f in files:
        print(path.join(folder_ref,f))




def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)




# The defualt range objct can only generate int
# This is an example of a range object for generating floats

def frange (start, stop=None, step=None):
    '''
    frange(stop) -> range from 0 to stop, incriment of 1 
    frange(start, stop) -> range from start to stop, incriment of 1 
    frange(start, stop, step) -> range from start to stop, incriment of step 
    start: start as a float, if this is the only inout specified it will be used as stop
    stop: stop as a float, range will stop when the next step would reach stop
    step: incriment as a float, defaults to 1 if omitted
    This is a range object for generating floats. It produces a sequence of floats from start (inclusive) to stop(exclusive) by step.
    '''

    # If step not set, use 1
    if not step:
        step = 1

    # if stop not set use 1
    if not stop:
        stop = start
        start = 0

    # Check for an infinite loop
    if (start > stop and step > 0) or (start < stop and step < 0):
        return start

    # Do the actual loop
    num = start
    count = 0
    while num < stop:
        yield num
        num = start + step*count
        count += 1



if __name__ == "__main__":

    file_name = r"\\Global.arup.com\london\BEL\Jobs\200000\249400\249439 Smithfield Poultry Market\5 External Data\01 Incoming Document Register\201106 Baseline Monitering Data\Smithfields_Market_20200921-20201030 - Tilts.csv"

    print(read_csv_file(file_name))