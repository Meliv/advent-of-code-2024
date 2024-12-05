import file_reader
from collections import defaultdict

FILE_NAME = 'files/day5.txt'

def get_valid_invalid() -> tuple[list[int],list[int]]:
    
    links = defaultdict(list)
    updates = list()

    for line in file_reader.read_file_as_list_str(FILE_NAME):
        if '|' in line:
            o = [int(x) for x in line.split('|')]
            links[o[0]].append(o[1])

        if ',' in line:
            updates.append([int(x) for x in line.split(',')])

    valid_updates = []
    invalid_updates = []

    for update in updates:
        valid = True
        for i, n in enumerate(update):
            if any([value for value in update[:i] if value in links[n]]):
                valid = False
            
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
            
    return valid_updates, invalid_updates
    
def part_one() -> int:
    valid_updates, _ = get_valid_invalid()
    return sum([x[int((len(x)-1)/2)] for x in valid_updates])

def part_two() -> int:
    
    visited = set() # Track visited nodes
    topological_order = [] # Store topological order
    graph = defaultdict(list[int])

    def topological_sort_dfs(graph, node):

        # Mark node as visited
        visited.add(node)

        # Recursively call DFS on its neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                    topological_sort_dfs(graph, neighbor)

        # Add node to topological order
        topological_order.append(node)
    
    ## Start
    for i in range(100):
        graph[i] = []

    input = [75,97,47,61,53]

    for line in file_reader.read_file_as_list_str(FILE_NAME):
        if '|' in line:
            o = [int(x) for x in line.split('|')]
            if o[0] in input and o[1] in input:
                graph[o[0]].append(o[1])
    
    for node in graph:
        if node not in visited and any(graph[node]):
            topological_sort_dfs(graph, node)
            
    print(list(reversed(topological_order)))
            
    return 0

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")