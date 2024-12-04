import re 
from functools import reduce

with open("input.txt") as f:
    text = f.read()

def eval_mul(s):
    return reduce(lambda a,b : a * b, [int(x) for x in s[4:-1].split(",")])

def part1():
    pattern = re.compile(r"mul\(\d+,\d+\)")
    found = re.findall(pattern, text)

    return sum([eval_mul(x) for x in found])

def part2():
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    found = re.findall(pattern, text)

    enable = 1
    res = 0
    for s in found:
        if s == "do()":
            enable = 1
        elif s == "don't()":
            enable = 0
        else:
            res += enable * eval_mul(s)

    return res 

print(part1())
print(part2())
