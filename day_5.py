from typing import DefaultDict, List, Tuple
import file_reader
from collections import defaultdict

FILE_NAME = 'files/day5.txt'
print('x')

def parse_input() -> tuple[defaultdict[list[int]], list[list[int]]]:
    
    orderings = defaultdict(list)
    updates = list()

    for line in file_reader.read_file_as_list_str(FILE_NAME):
        if '|' in line:
            o = [int(x) for x in line.split('|')]
            orderings[o[0]].append(o[1])

        if ',' in line:
            updates.append([int(x) for x in line.split(',')])
    
    return (orderings, updates)

def part_one() -> int:
    orderings, updates = parse_input()
    valid_updates = []

    for update in updates:
        valid = True
        for i, n in enumerate(update):
            if any([value for value in update[:i] if value in orderings[n]]):
                valid = False
                break
            
        if valid:
            valid_updates.append(update)

    return sum([x[int((len(x)-1)/2)] for x in valid_updates])

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")