import file_reader
import networkx as nx

FILE_NAME = 'files/day10.txt'

def part_one():
    print('x')
    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    G = nx.DiGraph()
    D = [(1,0),(-1,0),(0,1),(0,-1)]

    for y in range(len(input)-1):
        for x in range(len(input[y])-1):
            if input[y][x] == '.': continue
            G.add_node((y,x),value=int(input[y][x]))

            for d in D:
                n = input[y+d[0]][x+d[1]]
                if n != '.' and abs(int(input[y][x]) - int(n)) == 1:
                    G.add_edge((y,x), (y+d[0], x+d[1]))

    filtered_g = nx.DiGraph()
    for u, v in G.edges:
        if G.nodes[v]['value'] == G.nodes[u]['value'] + 1:
            filtered_g.add_edge(u, v, weight=1)

    sources = [n for n, d in G.nodes(data=True) if d['value'] == 0]
    targets = [n for n, d in G.nodes(data=True) if d['value'] == 9]

    all_paths = []
    for source in sources:
        for target in targets:
            try:
                p = nx.dijkstra_path(filtered_g, source, target)
                all_paths.append(p)
            except nx.NetworkXNoPath:
                continue

    return len(all_paths)

def part_two():
    input = file_reader.read_file_as_list_str(FILE_NAME)

    # Add padding
    for i in range(len(input)):
        input[i] = '.'+''.join(input[i])+'.'
    input.insert(0, '.'*len(input[0]))
    input.insert(len(input), '.'*len(input[0]))

    G = nx.DiGraph()
    D = [(1,0),(-1,0),(0,1),(0,-1)]

    for y in range(len(input)-1):
        for x in range(len(input[y])-1):
            if input[y][x] == '.': continue
            G.add_node((y,x),value=int(input[y][x]))

            for d in D:
                n = input[y+d[0]][x+d[1]]
                if n != '.' and abs(int(input[y][x]) - int(n)) == 1:
                    G.add_edge((y,x), (y+d[0], x+d[1]))

    def find_all_increasing_paths(graph, start, target_value):
        all_paths = []

        def dfs(current_node, current_path):
            current_value = graph.nodes[current_node]['value']
            
            if current_value == target_value:
                all_paths.append(list(current_path))
                return

            for neighbor in graph.neighbors(current_node):
                neighbor_value = graph.nodes[neighbor]['value']
                if neighbor_value == current_value + 1 and neighbor not in current_path:
                    dfs(neighbor, current_path + [neighbor])

        dfs(start, [start])
        return len(all_paths)

    all_paths = 0
    sources = [n for n, d in G.nodes(data=True) if d['value'] == 0]

    for source in sources:
        all_paths += find_all_increasing_paths(G, source, 9)

    return all_paths

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")