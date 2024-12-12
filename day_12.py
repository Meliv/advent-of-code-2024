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
    
        top_left = min(area_nodes, key=lambda cell: (cell[1], cell[0]))
        top_left = top_left[0], top_left[1], 0
    
        forward = [(0,1),(1,0),(0,-1),(-1,0)] #turning clockwise
        left =    [(-1,0),(0,1),(1,0),(0,-1)]
        
        current_y, current_x, d = top_left

        left_y, left_x = left[0]
        forward_y, forward_x = forward[0]
        vertices = 0
        
        while True:
            
            if input[current_y+left_y][current_x+left_x] == c:
                # Turn left
                d = (d-1)%4
                vertices += 1
                
                
                if (current_y, current_x, d) == top_left:
                    break
                
                left_y, left_x = left[d]
                forward_y, forward_x = forward[d]     
                
                current_y, current_x = current_y+forward_y,current_x+forward_x
            
                continue
            elif input[current_y+forward_y][current_x+forward_x] != c:
                # Turn right
                d = (d+1)%4
                vertices += 1
                
                
                if (current_y, current_x, d) == top_left:
                    break
                
                left_y, left_x = left[d]
                forward_y, forward_x = forward[d]     
                
                
                
                continue

            # Move forward            
            current_y, current_x = current_y+forward_y,current_x+forward_x

            if (current_y, current_x, d) == top_left:
                break
            
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
    
    print(f'part 2: {part_two}')
    return price

def part_two():
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")