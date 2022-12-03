from collections import Counter as c
items = []
"""
part 1
with open("./input.txt") as file:
    for line in file:
        firsthalf = set(line[:len(line) // 2])
        secondhalf = set(line[len(line) // 2: -1])
        for item in firsthalf:
            if item in secondhalf:
                items.append(item)
ans = ([ord(item) - 96 if item.islower() else ord(item) - ord('A') + 27 for item in items])
print(sum(ans))
"""


''''part 2'''
with open("./input.txt") as file:
    groups = []
    temp = []
    for line in file:
        if len(temp) == 3:
            groups.append(temp)
            temp = [set(line.rstrip())]
        else:
            temp.append(set(line.rstrip()))
groups.append(temp)
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            items.append(item)
print(sum(([ord(item) - 96 if item.islower() else ord(item) - ord('A') + 27 for item in items])))