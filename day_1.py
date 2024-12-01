import file_reader

def part_one(values: list[str]):
    left = list()
    right = list()

    for value in values:
        nums = value.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left.sort()
    right.sort()

    sum = 0
    for i in range(0, len(values)):
        sum += abs(left[i] - right[i])

    return sum

def part_two(values: list[str]):
    return 0

values = file_reader.read_file('files/day1.txt')

print(f"Part One: {part_one(values)}")
print(f"Part Two: {part_two(values)}")


print(sum)