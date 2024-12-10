import random
import file_reader

FILE_NAME = 'files/day9.txt'

def part_one():

    input = file_reader.read_file_as_str(FILE_NAME)
    memory = []

    for i,c in enumerate(input):
        memory.extend(['.']*int(c) if i%2 else [str(i//2)]*int(c))

    q = [(i) for i,x in enumerate(memory) if x == '.']
    
    for i,c in enumerate(memory[::-1]):
        if c == '.': continue
        x = q.pop(0)
        if x >= len(memory)-i: break
        memory[x] = c
        memory[-1-i] = '.'
        if not any(q): break

    return sum((i*int(c) for i,c in enumerate(memory) if c != '.'))

def part_two():

    input = file_reader.read_file_as_str(FILE_NAME)
        
    #memory[0] = 'Char . 0 9 etc'
    #memory[1] = 'Size of block'
    #memory[2] = 'Position in memory'
    memory = [('.' if i%2 else str(i//2), int(c), i) for i,c in enumerate(input)]
    
    #print
    #x = [m[0]*m[1] for m in memory]
    #print(''.join(x))
    
    #print('-----')
    
    #0 char
    #1 size
    #2 position in memory-grouping
    files = [(f[0],f[1]) for f in memory if f[0] != '.']
    
    for f in files[::-1]:
        s = next(((s[0],s[1],i) for i,s in enumerate(memory) if s[0] == '.' and s[1] >= f[1]), None)
        if s is not None:
            f_latest = next(len(memory)-i-1 for i,fm in enumerate(memory[::-1]) if fm[0] == f[0])
            if f_latest <= s[2]: continue

            memory[f_latest] = (s[0], f[1], f_latest)

            # Insert file, insert new spacing if needed            
            memory[s[2]] = (f[0],f[1],s[2])
            if s[1] != f[1]:
                memory.insert(s[2]+1, ('.',s[1]-f[1], s[2]+1))

            
            #print
            #x = [m[0]*m[1] for m in memory]
            #print(''.join(x))
    
                
    #s = [m[0]*m[1] for m in memory]
    
    #print(''.join(s))
    #print('----')
    #print('00992111777.44.333....5555.6666.....8888..')

    m = ''.join([m[0]*m[1] for m in memory])
    return sum((i*int(c) for i,c in enumerate(m) if c != '.'))

print(f"Day 9")
print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")