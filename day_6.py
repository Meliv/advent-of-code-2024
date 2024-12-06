import file_reader

'''
All credit to https://github.com/tmo1/adventofcode/blob/main/2024/06b.py on this one
I caved after I couldn't get the right result. Turns out I was only about 4 off
I took a look to see what other people were doing and found that page
They were doing exactly the same as what I was doing except they'd identified fixed one
minor bug that I'd missed.
When I was finding an obstacle, I was turning and moving which means my tracking set
was always short by as many turns in the path. It was throwing off a few edge cases

I don't feel bad about it. Logically I had it and this script has taught me
a lot about abusing tuples. I was going way OTT using classes. Bad C# habits
'''

FILE_NAME = 'files/day6.txt'

def part_one():
    tiles, visited = file_reader.read_file_as_list_str(FILE_NAME), set()
    n = ''.join(tiles).find('^')
    x_start, y_start = n % 10, n // 10
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    x, y, d = x_start, y_start, 0
    while True:
        visited.add((x,y))
        x1,y1 = x + directions[d][0], y + directions[d][1]
        if not (0 <= x1 < 10 and 0 <= y1 < 10):
            return len(visited)
        if tiles[y1][x1] == '#':
            d = (d + 1) % 4
        x,y = x + directions[d][0], y + directions[d][1]


def part_two():
    tiles, locations, total = file_reader.read_file_as_list_str(FILE_NAME), set(), 0
    n = ''.join(tiles).find('^')
    x_start, y_start = n % 10, n // 10
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    x, y, d = x_start, y_start, 0
    while True:
        locations.add((x,y))
        x1,y1 = x + directions[d][0], y + directions[d][1]
        if not (0 <= x1 < 10 and 0 <= y1 < 10):
            break
        if tiles[y1][x1] == '#':
            d = (d + 1) % 4
        x,y = x + directions[d][0], y + directions[d][1]
    for location in locations:
        x, y, d, visited = x_start, y_start, 0, set()
        while True:
            if (x, y, d) in visited:
                total += 1
                break
            visited.add((x,y,d))
            x1,y1 = x + directions[d][0], y + directions[d][1]
            if not (0 <= x1 < 10 and 0 <= y1 < 10):
                break
            if tiles[y1][x1] == '#' or (x1, y1) == location:
                d = (d + 1) % 4
            else:
                x,y = x + directions[d][0], y + directions[d][1]

    return total

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")