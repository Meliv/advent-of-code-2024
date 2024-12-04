from collections import defaultdict
import file_reader

input: list[str] = file_reader.read_file_as_list_str('files/day4.txt')

def part_one() -> int:
    def get_diagonal(input) -> str:
        key_values = defaultdict(str)
        for y in range(len(input)):
            for x in range(len(input[0])-1,-1,-1):
                key_values[x+y] += input[y][x]

        return key_values.values()

    rotated_input = [''.join(row) for row in zip(*input[::-1])]
    lines = ','.join([
        ','.join(input)                         # Horizontal
        ,','.join(rotated_input)                # Vertical
        ,','.join(get_diagonal(input))          # Diagonal /
        ,','.join(get_diagonal(rotated_input))  # Diagonal \
    ])

    return lines.count('XMAS') + lines.count('SAMX')

def part_two() -> int:
    result = 0
    for y in range(1, len(input)-1):
        for x in range(1, len(input[0])-1):
            if input[y][x] != 'A': continue
            result += int(all(x in ['SM','MS'] for x in [input[y-1][x-1]+input[y+1][x+1], input[y-1][x+1]+input[y+1][x-1]]))
    return result

print()
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")