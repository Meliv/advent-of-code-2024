from collections import defaultdict
import file_reader

input: list[str] = file_reader.read_file_as_list_str('files/day4.txt')

def part_one() -> int:
    rotated_input = [''.join(row) for row in zip(*input[::-1])]
    lines = ','.join([
        ','.join(input)                         # Horizontal
        ,','.join(rotated_input)                # Vertical
        ,','.join(get_diagonal(input))          # Diagonal /
        ,','.join(get_diagonal(rotated_input))  # Diagonal \
    ])

    return lines.count('XMAS') + lines.count('SAMX')


def part_two() -> int:
    return 0

def get_diagonal(input) -> str:
    key_values = defaultdict(str)
    for y in range(len(input)):
        for x in range(len(input[0])-1,-1,-1):
            key_values[x+y] += input[y][x]

    return key_values.values()

print()
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")