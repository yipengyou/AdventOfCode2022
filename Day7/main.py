directories = {}
currentDirectory = '/'
with open('./input.txt') as file:
    for line in file:
        if 'cd' in line:
            currentDirectory = line.rstrip()[5:]
        elif 'ls' in line:
            continue
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
    for a in i:
        if type(a) == int:
            temp += a
        else:
            return totalsize(a, temp)
    return temp
ans = []
for i in directories:
    ans.append(totalsize(i, 0))
print(ans)