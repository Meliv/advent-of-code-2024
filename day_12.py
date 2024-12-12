import file_reader

FILE_NAME = 'files/day12.txt'

def part_one():

    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    processed_nodes, price = set(), 0

    def flood_fill(input, x, y, c, area_nodes):
        if input[y][x] != c:
            return 1
            
        if (y,x) in processed_nodes:
            return 0
            
        area_nodes.append((y,x))
        processed_nodes.add((y,x))

        fences_needed = 0

        fences_needed += flood_fill(input, x, y+1, c, area_nodes)
        fences_needed += flood_fill(input, x, y-1, c, area_nodes)
        fences_needed += flood_fill(input, x-1, y, c, area_nodes)
        fences_needed += flood_fill(input, x+1, y, c, area_nodes)
        
        return fences_needed

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '.' or (y,x) in processed_nodes:
                continue
            
            area_nodes = []
            fences = flood_fill(input, x, y, input[y][x], area_nodes)
            price += len(area_nodes) * fences 
    
    return price

def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")