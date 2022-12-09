directories = {}
currentDirectory = '/'
with open('./input.txt') as file:
    for line in file:
        if "$ cd .." in line or "$ ls" in line:
            continue
        if 'cd' in line:
            currentDirectory = line.rstrip()[5:]
        elif "dir" in line:
            if currentDirectory in directories:
                directories[currentDirectory].append(line.rstrip()[4:])
            else:
                directories[currentDirectory] = [line.rstrip()[4:]]
        else:
            if currentDirectory in directories:
                directories[currentDirectory].append(int(line.rstrip().split(' ')[0]))
            else:
                directories[currentDirectory] = [int(line.rstrip().split(' ')[0])]

def totalsize(i, temp):
    for a in directories[i]:
        if type(a) == int:
            temp += a
        else:
            temp += totalsize(a, temp)
    return temp

ans = []

print(directories)
for a in directories:
    print(a)
    ans.append(totalsize(a, 0))
    
print(ans)
print(sum([a for a in ans if a <= 100000]))