data = ''
with open("./input.txt") as file:
    for line in file:
        data = line.rstrip()
data = list(data)
detectWindow = data[0:14]
for i, a in enumerate(data[14:]):
    detectWindow.pop(0)
    detectWindow.append(a)
    if len(detectWindow) == len(set(detectWindow)):
        print(i + 15)
        break
    