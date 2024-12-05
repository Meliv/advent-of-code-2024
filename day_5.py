from typing import DefaultDict, List, Tuple
import file_reader
from collections import defaultdict

FILE_NAME = 'files/day5.txt'
print('x')

def parse_input() -> tuple[defaultdict[list[int]], list[list[int]]]:
    
    input = file_reader.read_file_as_list_str(FILE_NAME)

    orderings = defaultdict(list)
    updates = list()

    for line in input:
        if '|' in line:
            o = [int(x) for x in line.split('|')]
            orderings[o[0]].append(o[1])

        if ',' in line:
            updates.append([int(x) for x in line.split(',')])
    
    return (orderings, updates)

def part_one() -> int:
    def get_valid_updates():
        
        for update in updates:
            for i,j in enumerate(update):
                
                n_before = update[:i]

                valid = set(orderings[j])

                if not valid.isdisjoint(n_before):
                    print(f'Invalid: {n_before}')
                else:
                    print(f'Valid: {n_before}')
            


    return 0

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")