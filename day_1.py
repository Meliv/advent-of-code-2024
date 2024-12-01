import file_reader
from collections import defaultdict

FILE_NAME = 'files/day1.txt'

def part_one() -> int:
    file_lines = file_reader.read_file(FILE_NAME)
    file_len = len(file_lines)

    left = [int(file_lines[l].split()[0]) for l in range(0,file_len)]
    right = [int(file_lines[l].split()[1]) for l in range(0,file_len)]

    left.sort()
    right.sort()

    return sum(abs(left[i] - right[i]) for i in range(0,file_len))

    
def part_two() -> int:
    file_lines = file_reader.read_file(FILE_NAME)
    file_len = len(file_lines)

    left = [int(file_lines[l].split()[0]) for l in range(0,file_len)]
    right = [int(file_lines[l].split()[1]) for l in range(0,file_len)]

    key_values = defaultdict(int)

    for i in range(0, file_len):
        key_values[left[i]] += right.count(left[i]) * left[i]

    return sum(key_values.values())


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")