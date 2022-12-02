scoring = {"rock": 1, 'paper': 2, "sizor": 3}
mapping = {'A':'rock', 'X' : 0, 'B' : "paper", 'Y': 3, 'C':'sizor', 'Z': 6}
turns = []
with open ("./input.txt") as file:
    for line in file:
        turns.append([mapping[line.rstrip().split(" ")[0]], mapping[line.rstrip().split(" ")[1]]])
answer = 0
for turn in turns:
    if turn[1] == 0:
        answer += (scoring[turn[0]] + 1) % 3 + 1
    elif turn[1] == 3:
        answer += 3 + scoring[turn[0]]
    else:
        answer += 6 + (scoring[turn[0]] % 3) + 1
print(answer)