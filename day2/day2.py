with open('input.txt') as fp:
    reports = [[int(lvl) for lvl in s.split()] for s in fp.readlines()]

def is_safe(report):
    increasing, decreasing = True, True

    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
        
        if report[i] > report[i+1]:
            decreasing = False

        if report[i] < report[i+1]:
            increasing = False

    return increasing or decreasing

def part1():
    return len([x for x in reports if is_safe(x)])
        
def part2():
    res = 0
    for report in reports:
        if is_safe(report):
            res += 1
            continue

        for i in range(len(report)):
            trimmed_report = report[:i] + report[i+1:]
            if is_safe(trimmed_report):
                res += 1
                break 

    return res 

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
