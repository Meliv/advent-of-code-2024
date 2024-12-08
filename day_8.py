import file_reader
import re
from itertools import groupby, combinations

FILE_NAME = 'files/day8.txt'
REGEX = '[^.\n]'

def part_one():

    input = file_reader.read_file_as_str(FILE_NAME)
    line_len = len(input.split('\n')[0])
    input = input.replace('\n','')
    input_len = len(input)
    grouped = groupby([(m.start(), m.group()) for m in sorted(re.finditer(REGEX, input),key=lambda x:x.group())], key=lambda x: x[1])
    antinodes, chars = set(), set()
    
    chars.add('\n')
    
    for group in grouped:
        
        for a,b in combinations(list(group[1]), 2):
            chars.add(a[1])
            d = abs(a[0] - b[0])
            for ai in (x for x in [a[0]-d,b[0]+d] if 0 <= x <= input_len):
                antinodes.add(ai)

    #debug
    for i,c in enumerate(input):
        if i % line_len == 0:
            print()
            
        if i in antinodes and c not in chars:
            print('#',end='')
        else:
            print(c,end='')
            
    print(f'\nTotal Antinodes: {len(antinodes)}')

    return len(antinodes)

def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")