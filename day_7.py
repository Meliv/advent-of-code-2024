import file_reader
from itertools import product, pairwise

FILE_NAME = 'files/day7.txt'

def part_one():
    result, input = [], [(int(a.split(':')[0]),[int(b) for b in a.split(':')[1].split()]) for a in file_reader.read_file_as_list_str(FILE_NAME)]

    for a,b in input:
        for p in product([0,1], repeat=len(b)-1):
            t = b[0]
            for i,y in enumerate(b[1:]):
                if list(p)[i]: t = t*y
                else: t = t+y
            if t == a:
                result.append(a) 
                break
        
    return sum(result)


def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")