forest = []
with open('./input.txt') as file:
    for line in file:
        forest.append([int(i) for i in list(line.rstrip())])


def left(i, j):
    count = 0
    for t in forest[i][j-1:0:-1]:
        if forest[i][j] > t:
            count += 1
        else:
            break
    return count + 1

def right(i, j):
    count = 0
    for t in forest[i][j + 1: -1]:
        if forest[i][j] > t:
            count += 1
        else:
            break
    return count + 1
def up(i, j):
    count = 0
    for t in [forest[k][j] for k in range(i - 1, 0, -1)]:
        if forest[i][j] > t:
            count += 1
        else:
            break
    return count + 1
def down(i, j):
    count = 0
    for t in [forest[k][j] for k in range(i + 1, len(forest) - 1)]:
        if forest[i][j] > t:
            count += 1
        else:
            break
    return count + 1
    
ans = 0

for i, a in enumerate(forest[1:-1], 1):
    for j, b in enumerate(a[1:-1], 1):
        print(i, j, right(i,j), left(i, j), up(i, j), down(i, j))
        ans = max(right(i,j) * left(i, j) * up(i, j) * down(i, j), ans)
print(ans)