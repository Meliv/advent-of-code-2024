from enum import Enum
import file_reader
from collections import defaultdict

FILE_NAME = 'files/day6.txt'

def part_one():
    
    tiles, visited = file_reader.read_file_as_list_str(FILE_NAME), set()
    
    n = ''.join(tiles).find('^')
    x_start, y_start = n % 130, n // 130
    #
    # x_start, y_start = n % 10, n // 10
            
    
    '''
    def print_grid():
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            if Position(x,y,any) in visited:
                print('X', end='')
            else:
                print(tiles.get((x,y)).c, end='')
                
        print('\n')
        print(f'{current_position.x}, {current_position.y}')
        print()
        '''

    # Directions 0,1,2,3
    
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    x, y, d = x_start, y_start, 0
    
    while True:
        visited.add((x,y))
        
        #print_grid()
        
        x1,y1 = x + directions[d][0], y + directions[d][1]
        
        # Break if oob
        if not (0 <= x1 < 130 and 0 <= y1 < 130):
        #if not (0 <= x1 < 10 and 0 <= y1 < 10):
            return len(visited)
        
        if tiles[y1][x1] == '#':
            d = (d + 1) % 4
            
        x,y = x + directions[d][0], y + directions[d][1]
            
    return None


def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")