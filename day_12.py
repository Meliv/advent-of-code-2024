import file_reader

FILE_NAME = 'files/day12.txt'

def part_one():

    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    '''
    Flood-fill (node):
    1. If node is not Inside return.
    2. Set the node
    3. Perform Flood-fill one step to the south of node.
    4. Perform Flood-fill one step to the north of node
    5. Perform Flood-fill one step to the west of node
    6. Perform Flood-fill one step to the east of node
    7. Return.
    '''
    
    processed_nodes = []
    shapes = []
    
    def flood_fill(input, x, y, c, filled_nodes):
        if input[y][x] != c or (x,y) in processed_nodes:
            return filled_nodes
        
        processed_nodes.append((x,y))
        
        flood_fill(input, x, y+1, c, filled_nodes)
        flood_fill(input, x, y-1, c, filled_nodes)
        flood_fill(input, x-1, y, c, filled_nodes)
        flood_fill(input, x+1, y, c, filled_nodes)
        
        filled_nodes.append((x,y))
        return filled_nodes

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '.' or (x,y) in processed_nodes:
                continue
            
            filled_nodes = flood_fill(input, x, y, input[y][x], [])
            
            if any(filled_nodes):
                shapes.append(filled_nodes)

    # Work out perimeters here
    
    return 0

def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")