import file_reader

FILE_NAME = 'files/day12.txt'

def part_one():

    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    return 0

def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")