import file_reader
from itertools import pairwise

FILE_NAME = 'files/day2.txt'
pairwise_check = lambda v: all(1 <= abs(a-b) <= 3 for a, b in pairwise(v))

input = [[int(i) for i in line] for line in [line.split() for line in file_reader.read_file(FILE_NAME)]]

def part_one() -> int:
    return len(list(filter(lambda x: (sorted(x) == x or sorted(x, reverse=True) == x) and pairwise_check(x), input)))

def part_two() -> int:
    valid_reports = 0
    
    for line in input:
        excluded = [[x for j, x in enumerate(line) if j != i] for i in range(len(line))]
    
        find_valid_reports = lambda x: (sorted(x) == x or sorted(x, reverse=True) == x) and pairwise_check(x)

        valid_reports += int(any(filter(find_valid_reports, excluded)))

    return valid_reports

print()
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")