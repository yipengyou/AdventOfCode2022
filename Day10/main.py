count = 1
sprite = 1
crt = [['.' for i in range(40)].copy() for i in range(6)]
with open("./input.txt") as file:
    for line in file:
        if count % 40 in range(sprite - 1, sprite + 2):
            crt[count // 40][count % 40] = '#'
        if "noop" in line:
            count += 1
        else:
            count += 1
            if count % 40 in range(sprite - 1, sprite + 2):
                crt[count // 40][count % 40] = '#'
            count += 1
            sprite += int(line[5:])
print(crt)