import file_reader
from itertools import pairwise

FILE_NAME = 'files/day2.txt'

def part_one() -> int:
    def pairwise_check(values) -> bool:
        for a,b in pairwise(values):
            if abs(a-b) < 1 or abs(a-b) > 3:
                return False     
        return True

    return len(list(filter(lambda x: (sorted(x) == x or sorted(x, reverse=True) == x) and pairwise_check(x) , read_input())))

def part_two() -> int:
    return 0

def read_input() -> list[list[int]]:
    file_lines = file_reader.read_file(FILE_NAME)
    return [[int(i) for i in line] for line in [line.split() for line in file_lines]]


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")