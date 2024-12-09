from queue import Queue
import file_reader

FILE_NAME = 'files/day9.txt'

def part_one():
    print('x')
    input = file_reader.read_file_as_str(FILE_NAME)
    memory = []

    for i,c in enumerate(input):
        memory.extend(['.']*int(c) if i%2 else [str(i//2)]*int(c))

    q = Queue()
    [q.put(i) for i,x in enumerate(memory) if x == '.']
    
    for i,c in enumerate(memory[::-1]):
        if c == '.': continue
        x = q.get()
        if x >= len(memory)-i: break
        memory[x] = c
        memory[-1-i] = '.'
        if q.empty(): break

    return sum((i*int(c) for i,c in enumerate(memory) if c != '.'))

def part_two():
    input = file_reader.read_file_as_str(FILE_NAME)
    
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")