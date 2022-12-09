directories = {}
currentDirectory = '/'
with open('./input.txt') as file:
    for line in file:
        if "$ cd .." in line or "$ ls" in line:
            pass
        elif '$ cd ' in line:
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

cache = {}
def totalsize(i, temp):
    if i in cache:
        return cache[i]
    else:
        for a in directories[i]:
            if type(a) == int:
                temp += a
            else:
                cache[i] = temp + totalsize(a, temp)
        return temp

ans = []

for a in directories:
    ans.append(totalsize(a, 0))
    
print(ans)
print(sum([a for a in ans if a <= 100000]))