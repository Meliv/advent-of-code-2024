import file_reader

FILE_NAME = 'files/day9.txt'

def part_one():
    input = file_reader.read_file_as_str(FILE_NAME)
    print('x') #Debug

    memory, defragged = [], []

    for i,c in enumerate(input):
        memory.extend(['.']*int(c) if i%2 else [str(i//2)]*int(c))

    # Defrag here

    for a in memory[::-1]:
        print(a,end='')

    print()

    # End defrag

    return sum((i*int(c) for i,c in enumerate(defragged) if c != '.'))

def part_two():
    input = file_reader.read_file_as_str(FILE_NAME)
    
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")