import file_reader
from collections import defaultdict

FILE_NAME = 'files/day5.txt'

def get_order(sequence, all_nodes) -> list[int]:
    visited = set()
    topological_order = []
    
    graph = defaultdict(list[int])
    for i in range(100): graph[i] = []
 
    def topological_sort_dfs(graph, node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                topological_sort_dfs(graph, neighbor)
        topological_order.append(node)

    for node in all_nodes:
        if node[0] in sequence and node[1] in sequence:
            graph[node[0]].append(node[1])   
                
    for node in graph:
        if node not in visited and any(graph[node]):
            topological_sort_dfs(graph, node)
        
    return list(reversed(topological_order))

def parse_input() -> tuple[list,defaultdict[list[int]]]:
    sequences = list()
    all_nodes = list()

    for line in file_reader.read_file_as_list_str(FILE_NAME):
        if '|' in line:
            all_nodes.append([int(x) for x in line.split('|')])

        if ',' in line:
            sequences.append([int(x) for x in line.split(',')])
    
    return all_nodes, sequences

def get_valid_invalid() -> tuple[list[int],list[int]]:
    all_nodes, sequences = parse_input()
    valid_updates = []
    ordered_invalid_updates = []

    for sequence in sequences:
        ordered = get_order(sequence, all_nodes)
        if sequence == ordered:
            valid_updates.append(sequence)
        else:
            ordered_invalid_updates.append(ordered)
            
    return valid_updates, ordered_invalid_updates
    
def part_one() -> int:
    valid, _ = get_valid_invalid()
    return sum([x[int((len(x)-1)/2)] for x in valid])

def part_two() -> int:
    _, ordered_invalid = get_valid_invalid()
            
    return sum([x[int((len(x)-1)/2)] for x in ordered_invalid])

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")