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
    
    def get_sides(area_nodes, c):
    
        vertices = 0
        
        rot_dir = [
            ((0,-1),(-1,-1),(-1,0)),
            ((-1,0),(-1,1),(0,1)),
            ((0,1),(1,1),(1,0)),
            ((1,0),(1,-1),(0,-1)),
            ]
        
        
        for y_node,x_node in area_nodes:
            
            for first, second, third in rot_dir:

                f_node = input[y_node+first[0]][x_node+first[1]]    
                s_node = input[y_node+second[0]][x_node+second[1]]    
                t_node = input[y_node+third[0]][x_node+third[1]]
                
                # Corner angle
                if f_node == c and s_node != c and t_node == c:
                    vertices += 1
                    
                # Outer corner angle
                if f_node != c and s_node != c and t_node != c:
                    vertices += 1
                    
                # Weird diagonal
                if f_node != c and s_node == c and t_node != c:
                    vertices += 1
            
    
        return vertices

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


    part_two = 0

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '.' or (y,x) in processed_nodes:
                continue
            
            area_nodes = []
            fences = flood_fill(input, x, y, input[y][x], area_nodes)
            price += len(area_nodes) * fences 
            
            n_sides = get_sides(area_nodes, input[y][x])
            
            part_two += n_sides * len(area_nodes)
            
            pass
    
    return price

def part_two():
    
    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    processed_nodes, price = set(), 0
    
    def get_sides(area_nodes, c):
    
        vertices = 0
        
        rot_dir = [
            ((0,-1),(-1,-1),(-1,0)),
            ((-1,0),(-1,1),(0,1)),
            ((0,1),(1,1),(1,0)),
            ((1,0),(1,-1),(0,-1)),
            ]
        
        
        for y_node,x_node in area_nodes:
            
            for first, second, third in rot_dir:

                f_node = input[y_node+first[0]][x_node+first[1]]    
                s_node = input[y_node+second[0]][x_node+second[1]]    
                t_node = input[y_node+third[0]][x_node+third[1]]
                
                # Corner angle
                if f_node == c and s_node != c and t_node == c:
                    vertices += 1
                    
                # Outer corner angle
                if f_node != c and s_node != c and t_node != c:
                    vertices += 1
                    
                # Weird diagonal
                if f_node != c and s_node == c and t_node != c:
                    vertices += 1
            
    
        return vertices

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
            
            n_sides = get_sides(area_nodes, input[y][x])
            
            price += n_sides * len(area_nodes)
            
            pass
    
    return price

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")