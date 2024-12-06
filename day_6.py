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
        
    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class Tile():
    def __init__(self, c):
        self.c = c


def part_one() -> int:

    tiles: dict[tuple[int,int],Tile] = {}
    unique_visited = set()
    visited: list[Position] = []
    
    def print_grid():
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            if Position(x,y,any) in unique_visited:
                print('X', end='')
            else:
                print(tiles.get((x,y)).c, end='')
                
        print('\n')
        print(f'{current_position.x}, {current_position.y}')
        print()
        

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
            if current_position not in unique_visited:
                unique_visited.add(current_position)
            else:
                pass
            
            visited.append(current_position)
            
            print_grid()
                
            current_position = get_next_position(current_position)
    except:
        pass

    print()
    print(f"Part 1: Unique Visits {len(unique_visited)}")
    print(f"Part 2: Visits {len(visited)}")
    
    return len(unique_visited)

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")