from copy import copy
from functools import cache

with open("input.txt") as fobj:
    stones = [int(x) for x in fobj.readline().split()]

def part1():
    st = copy(stones)
    temp = []
    for _ in range(25):
        temp = []
        for stone in st:
            s = str(stone)

            if stone == 0:
                temp.append(1)

            elif len(s) % 2 == 0:
                mid = len(s) // 2
                temp.append(int(s[:mid]))
                temp.append(int(s[mid:]))
                
            else:
                temp.append(stone * 2024)

        st = temp

    return len(st)

@cache
def recurse(stone,maximum, count=0):
    s = str(stone)

    if count == maximum:
        return 1

    if stone == 0:
        return recurse(1, maximum, count + 1)

    elif len(s) % 2 == 0:
        mid = len(s) // 2
        l, r = int(s[:mid]), int(s[mid:])
        return recurse(l, maximum, count+1) + recurse(r, maximum, count+1)
        
    else:
        return recurse(stone * 2024, maximum, count + 1)

def part2():
    res = 0
    for stone in stones:
        add = recurse(stone, 6)
        res += add

    return res

        
print(f"part1: {part1()}")
print(f"part2: {part2()}")
