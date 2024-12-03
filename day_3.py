import file_reader
import re

REGEX_STR_P1 = r'mul\(([0-9]{1,3},[0-9]{1,3})\)'
REGEX_STR_P2 = r'do\(\)|don\'t\(\)|(?:mul\(\d{1,3},\d{1,3})\)'

input_p1 = file_reader.read_file_as_str('files/day3_1.txt')
input_p2 = file_reader.read_file_as_str('files/day3_2.txt')

def part_one() -> int:
    return sum([int(x[0])*int(x[1]) for x in [match.split(',') for match in re.findall(REGEX_STR_P1, input_p1)]])

def part_two() -> int:
    result = 0
    capture = True

    for match in re.findall(REGEX_STR_P2, input_p2):
        if match.startswith('mul(') and capture:
            split = match.replace('mul(', '').replace(')', '').split(',')
            result += int(split[0]) * int(split[1])
        elif match == 'do()':
            capture = True
        else:
            capture = False

    return result

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")