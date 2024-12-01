import file_reader
from collections import defaultdict

def part_one(values: list[str]) -> int:
    left = list()
    right = list()

    for value in values:
        nums = value.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left.sort()
    right.sort()

    return sum(abs(left[i] - right[i]) for i in range(0,len(values)))

def part_two(values: list[str]) -> int:
    left = list()
    right = list()

    for value in values:
        nums = value.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    key_values = defaultdict(int)

    for i in range(0, len(values)):
        key_values[left[i]] += right.count(left[i]) * left[i]

    return sum(key_values.values())


values = file_reader.read_file('files/day1.txt')

print(f"Part One: {part_one(values)}")
print(f"Part Two: {part_two(values)}")