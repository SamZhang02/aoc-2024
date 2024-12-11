from pprint import pprint
import collections
from itertools import combinations

with open("input.txt") as fobj:
    map = [[_ for _ in line.strip()] for line in fobj.readlines()]

n, m = len(map), len(map[0])

def part1():

    def get_antinodes(coord1, coord2, n=1):
        coord1_to_coord2 = (coord2[0] - coord1[0], coord2[1] - coord1[1])
        coord2_to_coord1 = (coord1[0] - coord2[0], coord1[1] - coord2[1])

        antinode1 = coord1[0] + coord2_to_coord1[0], coord1[1] + coord2_to_coord1[1]
        antinode2 = coord2[0] + coord1_to_coord2[0], coord2[1] + coord1_to_coord2[1]
        return antinode1, antinode2

    antennas = collections.defaultdict(list)
    for i in range(n):
        for j in range(m):
            if map[i][j] != ".":
                antennas[map[i][j]].append((i, j))

    antenna_combinations = []
    for k,v in antennas.items():
        antenna_combinations += list(combinations(v, r=2))

    antinodes = set()
    for pair in antenna_combinations:
        antinode = get_antinodes(pair[0],pair[1])
        for a in antinode:
            if 0 <= a[0] < n and 0 <= a[1] < m:
                antinodes.add(a)
    
    return len(antinodes)

def part2():
    def get_antinodes(coord1, coord2):
        coord1_to_coord2 = (coord2[0] - coord1[0], coord2[1] - coord1[1])
        coord2_to_coord1 = (coord1[0] - coord2[0], coord1[1] - coord2[1])

        antinodes = []
        x = coord1[0]
        y = coord1[1]
        while 0 <= x < n and 0 <= y < m:
            antinodes.append((x,y))
            x += coord2_to_coord1[0]
            y += coord2_to_coord1[1]

        x = coord2[0]
        y = coord2[1]
        while 0 <= x < n and 0 <= y < m:
            antinodes.append((x,y))
            x += coord1_to_coord2[0]
            y += coord1_to_coord2[1]

        return antinodes

    antennas = collections.defaultdict(list)
    for i in range(n):
        for j in range(m):
            if map[i][j] != ".":
                antennas[map[i][j]].append((i, j))

    antenna_combinations = []
    for k,v in antennas.items():
        antenna_combinations += list(combinations(v, r=2))

    antinodes = set()
    for pair in antenna_combinations:
        for a in get_antinodes(pair[0],pair[1]):
            antinodes.add(a)
    print(antinodes)
    return len(antinodes)
    


print(f"part1: {part1()}")
print(f"part2: {part2()}")

