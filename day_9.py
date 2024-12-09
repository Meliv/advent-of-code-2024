import file_reader

FILE_NAME = 'files/day9.txt'

def part_one():
    input = file_reader.read_file_as_str(FILE_NAME)
    memory, defragged = [], []

    for i,c in enumerate(input):
        memory.extend(['.']*int(c) if i%2 else [str(i//2)]*int(c))

    # Defrag here
    x = False
    for i,a in enumerate(memory[::-1]):
        for j in range(len(memory)):
            if memory[j] == '.':
                memory[j] = a
                memory[-1-i] = '.'
                x = not any(y for y in memory[j+1:] if y != '.')

                break
        if x: break

        
    # End defrag

    return sum((i*int(c) for i,c in enumerate(defragged) if c != '.'))

def part_two():
    input = file_reader.read_file_as_str(FILE_NAME)
    
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")