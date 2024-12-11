from pprint import pprint
from functools import cache

with open("input.txt") as fobj:
    map = [[int(c) for c in line.strip()] for line in fobj.readlines()]

n, m = len(map), len(map[0])

directions = [(0,1), (1,0), (0, -1), (-1,0)]
def dfs(start, visited):
    x,y = start
    if map[x][y] == 9:
        return 

    for dx, dy in directions:
        if (
            0 <= x + dx < n 
            and 0 <= y + dy < m 
            and (x+dx, y+dy) not in visited 
            and map[x + dx][y + dy] == map[x][y] + 1
        ):
            visited.add((x + dx, y + dy))
            dfs((x + dx, y + dy), visited)


def part1():
    res = 0
    for i in range(n):
        for j in range(m):
            visited = set()
            if map[i][j] != 0:
                continue
            else:
                dfs((i,j), visited)
                res += len([(x,y) for x, y in visited if map[x][y] == 9])
    return res 

@cache
def dp(start):
    x,y = start
    if map[x][y] == 9:
        return 1

    res = 0
    for dx, dy in directions:
        if (
            0 <= x + dx < n 
            and 0 <= y + dy < m 
            and map[x + dx][y + dy] == map[x][y] + 1
        ):
            res += dp((x + dx, y + dy))

    return res 

def part2():
    res = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] != 0:
                continue
            else:
                res += dp((i,j))
    return res 

    

print(f"part1: {part1()}")
print(f"part2: {part2()}")
    

