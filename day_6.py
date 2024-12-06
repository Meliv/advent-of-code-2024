from enum import Enum
import file_reader
from collections import defaultdict

FILE_NAME = 'files/day6.txt'

class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3
    
class Cell:
    x: int
    y: int
    c: chr      

    def __init__(self, x: int, y: int, c: chr):
        self.x = x        
        self.y = y        
        self.c = c        
        
class Path:
    x: int
    y: int
    direction: Direction

    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction
    
class Map:
    cells: list[Cell]
    
    def __init__(self):
        self.cells = []
        for y, line in enumerate(file_reader.read_file_as_list_str(FILE_NAME)):
            for x, c in enumerate(line):
                self.cells.append(Cell(x, y, c))

    def print(self, patrolled_cells: set[Cell]):
        line_length = 10 #Needs to be updated for longer input
        for i,c in enumerate(self.cells):
            if i != 0 and i % line_length == 0:
                print()
                
            if any(filter(lambda ce: ce.x == c.x and ce.y == c.y, patrolled_cells)):
                print('X', end='')
            else:
                print(c.c, end='')
                
        print()
        
    def get_result(self, patrolled_cells: set[Cell]) -> int:
        result = 0
        
        for c in self.cells:
            if any(filter(lambda ce: ce.x == c.x and ce.y == c.y, patrolled_cells)):
                result += 1
                
        return result
    
    def get_tile(self, x: int, y: int) -> Cell:
        return [cell for cell in self.cells if cell.x == x and cell.y == y][0]
    
    def get_next_tile(self, path: Path) -> Cell:
        match path.direction:
            case Direction.North: return self.get_tile(path.x, path.y-1),
            case Direction.South: return self.get_tile(path.x, path.y+1),
            case Direction.East: return self.get_tile(path.x+1, path.y),
            case Direction.West: return self.get_tile(path.x-1, path.y),
            case _: raise Exception()
            
    def get_next_path(self, next_tile: Cell, path: Path) -> Path:
        new_path = Path(next_tile.x, next_tile.y, Direction.East)
        
        match next_tile.c, path.direction:
            case '#', Direction.North : new_path.direction = Direction.East,
            case '#', Direction.East : new_path.direction = Direction.South,
            case '#', Direction.South : new_path.direction = Direction.West,
            case '#', Direction.West : new_path.direction = Direction.North,
            case _: new_path.direction = path.direction
            
        return new_path
    
def part_one() -> int:

    map: Map = Map()
    
    map.print(set())  


    return 0

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")