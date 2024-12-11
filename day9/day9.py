import time 

with open("input.txt") as fobj:
    disk_map = fobj.read().strip()


def checksum(diskmap):
    res = 0
    for i,v in enumerate(diskmap):
        if v == "":
            continue
        res += v * i
    return res 

def part1():
    disk = []
    id = 0
    for i, v in enumerate(disk_map):
        for _ in range(int(v)):
            if i % 2 != 0:
                disk.append("")
            else:
                disk.append(id)
        if i % 2 != 0:
            id += 1

    l,r = 0, len(disk) - 1
    while l <= r:
        # print(l, r)
        if disk[r] != "" and disk[l] == "":
            disk[r], disk[l] = disk[l], disk[r]
            l += 1
            r -= 1
        elif disk[l] != "":
            l += 1
        elif disk[r] == "":
            r -= 1

    return checksum(disk)


def part2():
    disk = []
    id = 0
    for i, v in enumerate(disk_map):
        for _ in range(int(v)):
            if i % 2 != 0:
                disk.append("")
            else:
                disk.append(id)
        if i % 2 != 0:
            id += 1

    r = len(disk) - 1
    while r >= 0:
        print(r)
        if disk[r] == "":
            r -= 1
            continue

        l = r
        while l >= 0 and disk[l] != "" and disk[l] == disk[r]:
            l -= 1
        window_size = r-l

        for i in range(0, l):
            window = disk[i:i+window_size]
            if len(window) < window_size:
                continue

            if all([space == "" for space in window]):
                for j in range(i, i+window_size):
                    disk[j] = disk[r]

                for j in range(l+1, r+1):
                    disk[j] = ""

                break

        r = l

    return checksum(disk)


print(f"part1: {part1()}")
print(f"part2: {part2()}")

