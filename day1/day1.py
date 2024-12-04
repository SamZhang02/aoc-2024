from collections import Counter

arr1, arr2 = [], []

with open("input.txt", "r") as fp:
    for line in fp.readlines(): 
        a, b = [int(x) for x in line.split()]
        arr1.append(a)
        arr2.append(b)

counter = Counter(arr2)

arr1.sort()
arr2.sort()

res = 0
for a,b in zip(arr1, arr2):
    # res += abs(a - b) 
    res += a * counter[a]

print(res)

