from functools import cmp_to_key
from collections import defaultdict
from itertools import combinations, permutations
import multiprocessing
from multiprocessing import process

def process_permutation(perm):
    if is_correct(perm):
        return get_middle(perm)
    return None

with open("input.txt") as fobj:
    lines = [line.strip() for line in fobj.readlines()]

    rules = defaultdict(list)
    updates = []
    getting_rules = True
    for line in lines:
        if line == "":
            getting_rules = False
            continue

        if getting_rules:
            x, y = line.split("|")
            rules[int(x)].append(int(y))
        else:
            updates.append([int(n) for n in line.split(",")])
        
def is_correct(update):
    occured = set()
    for number in update:
        for prev in rules[number]:
            if prev in occured:
                return False
        occured.add(number)

    return True

def get_middle(arr):
    res = arr[len(arr) // 2]
    return res 
        

def part1():
    res = 0
    for update in updates:
        if is_correct(update):
            res += get_middle(update)
    return res 

def smaller(a,b):
    if a in rules and b in rules[a]:
        return -1
    return 0
    

def part2():
    res = 0

    update:list[int]
    for i, update in enumerate(updates):
        if not is_correct(update):
            reorder = sorted(update, key=cmp_to_key(smaller) )
            print(update, reorder, is_correct(reorder))
            res += get_middle(reorder)
            
    return res 


if __name__ == "__main__":
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
