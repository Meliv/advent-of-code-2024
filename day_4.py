import file_reader

input: list[str] = file_reader.read_file_as_list_str('files/day4.txt')

print('x')

def part_one() -> int:

    print(f'Total Chars: {len(''.join(input))}')

    horizontal = ','.join(input)
    vertical = ','.join([','.join(x) for x in list((zip(*input[::-1])))])
    diag_1 = ','.join(get_diagonal(input))
    diag_2 = ','.join(get_diagonal(list((zip(*input[::-1])))))

    arr = ','.join([horizontal, vertical, diag_1, diag_2])


    return arr.count('XMAS') + arr.count('SAMX')


def part_two() -> int:
    return 0

def get_diagonal(input) -> str:

    # Nasty but works. Needs tidying up or maybe even a full rethink. Def better ways to do it

    diag_joined = []

    h = len(input)
    w = len(input[0])

    diag_start = h-1

    backward = False

    # Step 1 - Y MAX -> 0
    while diag_start >= 0 and not (diag_start == 0 and backward):

        line = []

        if not backward:
            x = 0
            y = diag_start
        else:
            y = 0
            x = diag_start
        
        while y != h and x != w:
            line.append(input[y][x])
            x += 1
            y += 1
        
        diag_start -= 1

        if diag_start == -1 and not backward:
            diag_start = w-1
            backward = True

        diag_joined.append(''.join(line))

    return diag_joined

print()
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")