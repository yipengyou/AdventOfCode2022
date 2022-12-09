seen = {(0,0)}
currentdirection = 'R'
headpos = [0,0]
recentmoves = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
with open('./input.txt') as file:
    for line in file:
        direction = line.rstrip()[0]
        distance = int(line.rstrip()[2:])
        print(direction, distance)
        if direction == 'R':
            for i in range(distance):
                temp = recentmoves[0].copy()
                headpos[1] += 1
                recentmoves.append(headpos.copy())
                recentmoves.pop(0)
                for i in range(8):
                    if abs(recentmoves[i][1] - recentmoves[i + 1][1] > 1):
                        recentmoves[i] = recentmoves[i + 1].copy()
                if (recentmoves[0] != temp):
                    seen.add(tuple(temp))
        elif direction == 'L':
            for i in range(distance):
                temp = recentmoves[0].copy()
                headpos[1] -= 1
                recentmoves.append(headpos.copy())
                recentmoves.pop(0)
                for i in range(8):
                    if abs(recentmoves[i][1] - recentmoves[i + 1][1] > 1):
                        recentmoves[i] = recentmoves[i + 1].copy()
                if (recentmoves[0] != temp):
                    seen.add(tuple(temp))
        elif direction == 'U':
            for i in range(distance):
                temp = recentmoves[0].copy()
                headpos[0] += 1
                recentmoves.append(headpos.copy())
                recentmoves.pop(0)
                for i in range(8):
                    if abs(recentmoves[i][0] - recentmoves[i + 1][0] > 1):
                        recentmoves[i] = recentmoves[i + 1].copy()
                if (recentmoves[0] != temp):
                    seen.add(tuple(temp))
        elif direction == "D":
            for i in range(distance):
                temp = recentmoves[0].copy()
                headpos[0] -= 1
                recentmoves.append(headpos.copy())
                recentmoves.pop(0)
                for i in range(8):
                    if abs(recentmoves[i][0] - recentmoves[i + 1][0] > 1):
                        recentmoves[i] = recentmoves[i + 1].copy()
                if (recentmoves[0] != temp):
                    seen.add(tuple(temp))
print(seen)
print(len(seen))