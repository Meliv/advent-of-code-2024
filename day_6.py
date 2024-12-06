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
    
    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.x == other.x and self.y == other.y and self.c == other.c
        return False

    def __hash__(self):
        return hash((self.x, self.y, self.c))
        
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
    first_cell: Cell
    
    def __init__(self):
        self.cells = []
        for y, line in enumerate(file_reader.read_file_as_list_str(FILE_NAME)):
            for x, c in enumerate(line):
                cell = Cell(x,y,c)
                self.cells.append(cell)
                
                if cell.c == '^':
                    cell.c = 'X'
                    self.first_cell = cell

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
        return next(cell for cell in self.cells if cell.x == x and cell.y == y)
    
    def get_next_tile(self, current_position: Path) -> Cell:
        match current_position.direction:
            case Direction.North: return self.get_tile(current_position.x, current_position.y-1)
            case Direction.South: return self.get_tile(current_position.x, current_position.y+1)
            case Direction.East: return self.get_tile(current_position.x+1, current_position.y)
            case Direction.West: return self.get_tile(current_position.x-1, current_position.y)
            case _: raise Exception()
            
    def get_next_position(self, current_position: Path) -> Path:
        
        next_tile: Cell = self.get_next_tile(current_position)
        
        match next_tile.c, current_position.direction:
            case ('#', Direction.North) : current_position.direction = Direction.East
            case ('#', Direction.East) : current_position.direction = Direction.South
            case ('#', Direction.South) : current_position.direction = Direction.West
            case ('#', Direction.West) : current_position.direction = Direction.North
            case _: pass
            
        next_tile = self.get_next_tile(current_position)
        
        return Path(next_tile.x, next_tile.y, current_position.direction)
    
def part_one() -> int:

    map: Map = Map()
    
    patrolled_cells: set[Cell] = set()
    patrolled_cells.add(map.first_cell)
    
    current_path = Path(map.first_cell.x, map.first_cell.y, Direction.North)
    
    try:
        while True:
            next_path = map.get_next_position(current_path)
        
            patrolled_cells.add(Cell(next_path.x, next_path.y, 'X'))
        
            current_path = next_path
            
            # Debug
            #map.print(patrolled_cells)
    except:
        pass # This is lazy as hell I know

    return len(patrolled_cells)

def part_two() -> int:
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")