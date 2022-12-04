areas = []
with open("./input.txt") as file:
    for line in file:
        areas.append(line.rstrip().split(","))

one = 0
two = 0
three = 0
four = 0
answer = 0
for area in areas:
    one = int(area[0].split("-")[0])
    two = int(area[0].split("-")[1])
    three = int(area[1].split("-")[0])
    four = int(area[1].split("-")[1])
    if (one <= three and two >= four) or (one >= three and two <= four):
        answer += 1
print(answer)

"""part 2"""
answer = 0
for area in areas:
    one = int(area[0].split("-")[0])
    two = int(area[0].split("-")[1])
    three = int(area[1].split("-")[0])
    four = int(area[1].split("-")[1])
    if one < three:
        if two >= three:
            answer += 1
    elif one > three:
        if four >= one:
            answer += 1
    else:
        answer += 1
print(answer)