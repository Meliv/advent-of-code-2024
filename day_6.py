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
            
            #print_grid()
                
            current_position = get_next_position(current_position)
    except:
        pass

    print()
    return len(unique_visited)

def part_two() -> int:
    
    def print_grid(tiles: dict[tuple[int,int]]):
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            if Position(x,y,any) in visited:
                print('X', end='')
            else:
                print(tiles.get((x,y)).c, end='')
                
        print('\n')
        
    def print_grid_no_path(tiles: dict[tuple[int,int]]):
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            print(tiles.get((x,y)).c, end='')
                
        print('\n')
        
    def print_grid_no_path_current_position(tiles: dict[tuple[int,int]], cp: Position):
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                
            if cp.x == x and cp.y == y:
                print('X', end='')
            else: 
                print(tiles.get((x,y)).c, end='')
                
        print('\n')
        
    def populate_tiles(input, obstacle: Position = None) -> tuple[dict[tuple[int,int],Tile],Position]:
        tiles: dict[tuple[int,int],Tile] = {}
        
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '^':
                    tiles[(x,y)] = Tile('.')
                    start_position = Position(x, y, Direction.North)
                elif obstacle is not None and obstacle.x == x and obstacle.y == y:
                    tiles[(x,y)] = Tile('O')
                else:
                    tiles[(x,y)] = Tile(c)
                    
        return tiles, start_position
        

    def get_next_position(current_position: Position, tiles: dict[tuple[int,int]]) -> Position:

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
        
        hit_obstacle = next_tile.c == 'O'
        
        match next_tile.c, current_position.d:
            case '#'|'O', Direction.North:
                next_position = Position(current_position.x+1, current_position.y, Direction.East)            
            case '#'|'O', Direction.East:
                next_position = Position(current_position.x, current_position.y+1, Direction.South)            
            case '#'|'O', Direction.South:
                next_position = Position(current_position.x-1, current_position.y, Direction.West)            
            case '#'|'O', Direction.West:
                next_position = Position(current_position.x, current_position.y-1, Direction.North)            
            case _:
                pass

        return next_position, hit_obstacle      

    input = file_reader.read_file_as_list_str(FILE_NAME)
    tiles, current_position = populate_tiles(input)
    inf_loops = 0
    visited = set()
    original_path: list[Position] = []
    
    try:
        while True:

            if current_position not in visited:
                original_path.append(current_position)
                visited.add(current_position)
        
            current_position, _ = get_next_position(current_position, tiles)
    except:
        pass
        
    for i in range(0, len(original_path)-1):
        print(f"Run {i+1} of {len(original_path)}")
        
        '''     
        # Display the path for debugging
        for i,(x,y) in enumerate(tiles.keys()):
            if i != 0 and i % 10 == 0:
                print()
                    
            if Position(x,y,any) in path:
                print('X', end='')
            else:
                print(tiles.get((x,y)).c, end='')
        '''  
        
        
        # Insert obstacle
        obstacle = Position(original_path[i+1].x,original_path[i+1].y,any)
        tiles, _ = populate_tiles(input, obstacle)
        
        current_position = Position(original_path[i].x, original_path[i].y, original_path[i].d)
        
        
        #print_grid_no_path(tiles)
        #print(i)
        
        hit_obstacle = False
        max_cycle = 5000
        cycle = 0
        
        path = []
        
        # Reset start
        try:
            while True:

                #print_grid_no_path_current_position(tiles, current_position)  

                pass

                if len(list(filter(lambda xx: xx == current_position and xx.d == current_position.d, path))) > 1:
                    inf_loops += 1
                    #print_grid_no_path_current_position(tiles, current_position)  
                    #print(i)
                    break
                
                #print_grid_no_path(tiles)
                
                current_position, hit = get_next_position(current_position, tiles)
        
                path.append(current_position)
                cycle += 1
        except:
            pass

    return inf_loops

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")