from pprint import pprint
from copy import deepcopy
with open('input.txt') as fobj:
    map = [list(line.strip()) for line in fobj.readlines()]


directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
guard_positions = ["^", ">", "v", "<"]

def count_X(map):
    res = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "X":
                res += 1
    return res 

def part1():
    x, y = 0, 0
    direction = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in guard_positions:
                direction = guard_positions.index(map[i][j])
                x,y = i,j
                map[i][j] = "X"
                break


    while 0 <= x < len(map)-1 and 0<= y < len(map[0])-1:  
        dx = x + directions[direction][0]
        dy = y + directions[direction][1]
        if map[dx][dy] == "#":
            direction = (direction + 1) % 4
        else:
            map[dx][dy] = "X"
            x,y = dx, dy

    return count_X(map)

def part2():
    with open('input.txt') as fobj:
        map = [list(line.strip()) for line in fobj.readlines()]

    start_x, start_y = 0, 0
    start_direction = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in guard_positions:
                start_direction = guard_positions.index(map[i][j])
                start_x,start_y = i,j

    res = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(f"{i}/{len(map)}, {j}/{len(map[0])}")
            if (i, j) == (start_x, start_y) or map[i][j] == "#":
                continue
            
            x, y = start_x, start_y
            direction = start_direction
            map_copy = deepcopy(map)
            map_copy[i][j] = "#"

            # if the guard hit the same obstacle from the same direction hes cooked
            obstacle_hit = set() #tuple[obstacle coord, dir]

            while 0 <= x < len(map)-1 and 0<= y < len(map[0])-1:  
                dx = x + directions[direction][0]
                dy = y + directions[direction][1]
                if map_copy[dx][dy] == "#":
                    if ((dx,dy), direction) in obstacle_hit:
                        res += 1
                        break

                    obstacle_hit.add(((dx,dy), direction))
                    direction = (direction + 1) % 4
                else:
                    x, y = dx, dy
    return res 
     
#{((1, 4), 0), ((6, 8), 2), ((1, 8), 1), ((6, 4), 3)}

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
