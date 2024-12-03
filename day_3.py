import file_reader
import re

FILE_NAME = 'files/day3.txt'
REGEX_STR = 'mul\(([0-9]{1,3},[0-9]{1,3})\)'

input = file_reader.read_file_as_str(FILE_NAME)

def part_one() -> int:
    return sum([int(x[0])*int(x[1]) for x in [match.split(',') for match in re.findall(REGEX_STR, input)]])

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")