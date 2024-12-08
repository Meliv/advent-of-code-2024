import file_reader
import re
from itertools import groupby, combinations

FILE_NAME = 'files/day8.txt'
REGEX = '[^.\n]'

def part_one():

    input = file_reader.read_file_as_list_str(FILE_NAME)
    input_len, line_len = len(input), len(input[0])
    antinodes = set()
    grouped = groupby([((m.start()%line_len,m.start()//line_len), m.group()) for m in sorted(re.finditer(REGEX, ''.join(input)),key=lambda x:x.group())], key=lambda x: x[1])
    
    for group in grouped:
        for a,b in combinations(list(group[1]), 2):
        
            x1,x2 = a[0][0], b[0][0]
        
            y1,y2 = a[0][1], b[0][1]

            xV,yV = x2 - x1, y2 - y1
            
            x3,y3 = (x2 + xV, y2 + yV)        
            x4,y4 = (x1 - xV, y1 - yV)

            if x3 in range(line_len) and y3 in range(input_len):
                antinodes.add((x3,y3))                
            if x4 in range(line_len) and y4 in range(input_len):
                antinodes.add((x4,y4))    
            
    return len(antinodes)

def part_two():
    
    input = file_reader.read_file_as_list_str(FILE_NAME)
    input_len, line_len = len(input), len(input[0])
    antinodes = set()
    grouped = groupby([((m.start()%line_len,m.start()//line_len), m.group()) for m in sorted(re.finditer(REGEX, ''.join(input)),key=lambda x:x.group())], key=lambda x: x[1])
    
    for group in grouped:
        for a,b in combinations(list(group[1]), 2):
            m = 0
            while m < line_len and m < input_len:
                m += 1
                
                x1,x2 = a[0][0], b[0][0]
            
                y1,y2 = a[0][1], b[0][1]

                xV,yV = m*(x2 - x1), m*(y2 - y1)
                
                x3,y3 = (x2 + xV, y2 + yV)        
                x4,y4 = (x1 - xV, y1 - yV)
                
                antinodes.add((x1,y1))
                antinodes.add((x2,y2))
                
                if x3 in range(line_len) and y3 in range(input_len):
                    antinodes.add((x3,y3))
                if x4 in range(line_len) and y4 in range(input_len):
                    antinodes.add((x4,y4))

    return len(antinodes)

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")