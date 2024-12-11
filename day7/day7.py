import itertools 

with open("input.txt") as fobj:
    lines = [line.strip().split(":") for line in fobj.readlines()]

def eval_ltr(arr):
    sum = int(arr[0])
    for i in range(1, len(arr),2):
        op, nxt = arr[i:i+2]
        if op == "*":
            sum *= int(nxt)
        elif op == "+":
            sum += int(nxt)
        elif op == "||":
            sum = int(str(sum) + str(nxt))
    return sum 

def part1():
    res = 0
    for ans, nums in lines:
        nums = nums.strip().split()
        for perm in itertools.product(["+", "*"], repeat=len(nums) - 1):
            attempt = []
            for i in range(len(nums)-1):
                attempt.append(nums[i])
                attempt.append(perm[i])

            attempt.append(nums[-1])
            if eval_ltr(attempt) == int(ans):
                res += int(ans)
                break
    return res 

def part2():
    res = 0
    for ans, nums in lines:
        nums = nums.strip().split()
        for perm in itertools.product(["+", "*", "||"], repeat=len(nums) - 1):
            attempt = []
            for i in range(len(nums)-1):
                attempt.append(nums[i])
                attempt.append(perm[i])

            attempt.append(nums[-1])

            if eval_ltr(attempt) == int(ans):
                res += int(ans)
                break
    return res 

print(f"part1: {part1()}")
print(f"part2: {part2()}")

        
