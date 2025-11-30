import numpy as np
with open("day5_input.txt") as data:
    D = data.read().splitlines()

stacks = D[:8]
npstacks = np.array([[stacks[d][i] for i in range(1,len(stacks[d]),4)] for d in range(len(stacks))])
stacks = [list(i) for i in npstacks.transpose()]
for s in range(len(stacks)):
    stacks[s] = [i for i in stacks[s] if i != " "]
    stacks[s].reverse()

stacks_part2 = [[j for j in i] for i in stacks]


crane_moves = [i.split(" ") for i in D[10:]]
crane_moves = [[int(i[1]), int(i[3]), int(i[5])] for i in crane_moves]

for move in crane_moves:
    crates = stacks[move[1]-1][-move[0]:]
    crates.reverse()
    stacks[move[2]-1] += crates
    stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]

    crates_part2 = stacks_part2[move[1]-1][-move[0]:]
    stacks_part2[move[2]-1] += crates_part2
    stacks_part2[move[1]-1] = stacks_part2[move[1]-1][:-move[0]]

print("".join([i[-1] for i in stacks]))
print("".join([i[-1] for i in stacks_part2]))