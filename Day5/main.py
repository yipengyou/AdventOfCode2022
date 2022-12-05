"""puzzle input sucks so i'm cleaning it up manually in the code"""
stack1 = ['W','R','T','G'][::-1]
stack2 = ['W', 'V', 'S', 'M','P', 'H','C','G'][::-1]
stack3 = ['M','G','S','T','L','C'][::-1]
stack4 = ['F','R','W', 'M','D', 'H','J'][::-1]
stack5 = ['J','F','W','S','H','L','Q','P'][::-1]
stack6 = ['S','M','F','N','D','J','P'][::-1]
stack7 = ['J','S','C','G','F','D','B','Z'][::-1]
stack8 = ['B','T','R'][::-1]
stack9 = ['C','L','W','N','H'][::-1]
operations = []
with open('./input.txt') as file:
    for line in file:
        line = line.rstrip().split()
        temp = []
        for action in line:
            if action.isdigit():
                temp.append(int(action))
        operations.append(temp)
        
mappa = {1:stack1, 2:stack2, 3:stack3, 4:stack4, 5:stack5, 6:stack6, 7:stack7, 8:stack8, 9:stack9}

"""
for operation in operations:
    for i in range(operation[0]):
        mappa[operation[2]].append(mappa[operation[1]].pop())
"""
"""part2"""
for operation in operations:
    temp = mappa[operation[1]][-operation[0]:]
    mappa[operation[1]] = mappa[operation[1]][:-operation[0]]
    mappa[operation[2]] += (temp)
print(''.join([a[-1] for a in mappa.values()]))