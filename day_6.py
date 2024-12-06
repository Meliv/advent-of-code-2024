from enum import Enum
import file_reader
from collections import defaultdict

FILE_NAME = 'files/day6.txt'

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Position():
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

class Tile():
    def __init__(self, c):
        self.c = c


def part_one() -> int:

    tiles: dict[tuple[int,int],Tile] = {}
    visited = set()
    
    def print_grid():
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            if (x,y) in visited:
                print('X', end='')
            else:
                print(tiles.get((x,y)).c, end='')
                
        print('\n')

    def get_next_position(current_position: Position) -> Position:

        next_position = None
        match current_position.d:
            case Direction.North:
                next_position = Position(current_position.x, current_position.y-1, Direction.North)            
            case Direction.East:
                next_position = Position(current_position.x+1, current_position.y, Direction.East)            
            case Direction.South:
                next_position = Position(current_position.x, current_position.y+1, Direction.South)            
            case Direction.West:
                next_position = Position(current_position.x-1, current_position.y, Direction.West)
            case _:
                raise Exception()

        next_tile: Tile = tiles.get((next_position.x, next_position.y))
        
        match next_tile.c, current_position.d:
            case '#', Direction.North:
                next_position = Position(current_position.x+1, current_position.y, Direction.East)            
            case '#', Direction.East:
                next_position = Position(current_position.x, current_position.y+1, Direction.South)            
            case '#', Direction.South:
                next_position = Position(current_position.x-1, current_position.y, Direction.West)            
            case '#', Direction.West:
                next_position = Position(current_position.x, current_position.y-1, Direction.North)            
            case _:
                pass

        return next_position            

    current_position = None
    
    # Read all tiles, get start position
    for y, line in enumerate(file_reader.read_file_as_list_str(FILE_NAME)):
        for x, c in enumerate(line):
            tiles[(x,y)] = Tile(c)
            if c == '^':
                current_position = Position(x, y, Direction.North)
                
    try:
        while True:
            if (current_position.x, current_position.y) not in visited:
                visited.add((current_position.x, current_position.y))
            else:
                pass
            
            #print_grid()
                
            current_position = get_next_position(current_position)
    except:
        pass

    print()
    return len(visited)

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")