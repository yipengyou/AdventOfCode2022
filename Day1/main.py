elves = []
temp = []
with open("./input.txt") as file:
    for line in file:
        if line.strip() == "":
            elves.append(temp)
            temp = []
        else:
            temp.append(int(line.strip()))
answer = [0, 0, 0]
for elf in elves:
    temp = sum(elf)
    answer.append(temp)
    answer.sort()
    answer.pop(0)
print(sum(answer))