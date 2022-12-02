scoring = {"rock": 1, 'paper': 2, "sizor": 3}
mapping = {'A':'rock', 'X' : 'rock', 'B' : "paper", 'Y': 'paper', 'C':'sizor', 'Z': 'sizor'}
turns = []
with open ("./input.txt") as file:
    for line in file:
        turns.append([mapping[line.rstrip().split(" ")[0]], mapping[line.rstrip().split(" ")[1]]])
answer = 0
for turn in turns:
    if turn[0] == turn[1]:
        answer += 3 + scoring[turn[0]]
    else:
        if turn[1] == 'rock':
            if turn[0] == 'sizor':
                answer += 6 + 1
            else:
                answer += 1
        elif turn[1] == 'paper':
            if turn[0] == 'rock':
                answer += 8
            else:
                answer += 2
        elif turn[1] == 'sizor':
            if turn[0] == 'paper':
                answer += 9
            else:
                answer += 3
print(answer)