'''
for each x, y coord just check every possible one.

'''
grid = []
with open("input.txt", "r") as file:
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        grid.append(list(line))
m = len(grid)
n = len(grid[0])
print(grid)
dirs = {
    "up" : (-1, 0),
    "down" : (1, 0),
    "left" : (0, -1),
    "right" : (0, 1),
    "nw" : (-1, -1),
    "ne" : (-1, 1),
    "se" : (1, 1),
    "sw" : (1, -1),
}
def checkCoord(i_in, j_in):
    global grid
    matches = 0
    for name, dir in dirs.items():
        x, y = i_in, j_in
        valid = True
        for c in "XMAS":
            if x < 0 or x >= m or y < 0 or y >= n:
                valid = False
                break
            if grid[x][y] == c:
                x += dir[0]
                y += dir[1]
            else:
                valid = False
                break
        if valid:
            matches += 1
    return matches

total = 0

for i in range(m):
    for j in range(n):
        total += checkCoord(i, j)


print("Total ", total)
