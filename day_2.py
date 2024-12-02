import file_reader
from itertools import islice, pairwise
from collections import deque

FILE_NAME = 'files/day2.txt'

def part_one() -> int:
    def pairwise_check(values) -> bool:
        for a,b in pairwise(values):
            if abs(a-b) < 1 or abs(a-b) > 3:
                return False     
        return True

    return len(list(filter(lambda x: (sorted(x) == x or sorted(x, reverse=True) == x) and pairwise_check(x) , read_input())))

def part_two() -> int:
    def pairwise_check(values) -> bool:
        
        def get_window(values):
            iterator = iter(values)
            window = deque(islice(iterator, 2), maxlen=3)
            for x in iterator:
                window.append(x)
                yield tuple(window)

        for a,b,c in get_window(values):
            out_of_range = abs(a-b) < 1 or abs(a-b) > 3
            if out_of_range and (abs(a-c) < 1 or abs(a-c) > 3):
                print(f'{values} : False')
                return False 
            
        print(f'{values} : True')
        return True

    return len(list(filter(lambda x: pairwise_check(x) , read_input())))

def read_input() -> list[list[int]]:
    file_lines = file_reader.read_file(FILE_NAME)
    return [[int(i) for i in line] for line in [line.split() for line in file_lines]]


print()
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")