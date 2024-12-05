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

def checkCoord(i_in, j_in):
    global grid
    matches = 0

    x, y = i_in, j_in
    tl_br = False
    bl_tr = False
    
    if not (x + 1 < 0 or x + 1 >= m or y + 1 < 0 or y + 1 >= n) and not (x - 1 < 0 or x - 1 >= m or y - 1 < 0 or y - 1 >= n):
        if grid[x+1][y+1] in "MS" and grid[x-1][y-1] in "MS" and grid[x+1][y+1] != grid[x-1][y-1]:
            tl_br = True

    if not (x + 1 < 0 or x + 1 >= m or y - 1 < 0 or y - 1 >= n) and not (x - 1 < 0 or x - 1 >= m or y + 1 < 0 or y + 1 >= n):
        if grid[x+1][y-1] in "MS" and grid[x-1][y+1] in "MS" and grid[x+1][y-1] != grid[x-1][y+1]:
            bl_tr = True

    if tl_br and bl_tr:
        matches += 1
    return matches

total = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == "A":
            total += checkCoord(i, j)


print("Total ", total)
