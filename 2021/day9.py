data = open("day9_input.txt").read().splitlines()
D = [[9 for i in range(len(data[0])+2)] for k in range(len(data)+2)]

for i in range(len(data)):
    for k in range(len(data[0])):
        D[i+1][k+1] = int(data[i][k])

rl = 0
L=[]
for i in range(1,len(D)-1):
    for k in range(1,len(D[0])-1):
        if all(D[i][k] < l for l in [D[i+j][k] for j in [-1,1]] + [D[i][k+j] for j in [-1,1]]):
            rl += (D[i][k]+1)
            L.append((i,k))
print("part 1:", rl)

def basin(i, k, B):
    B.append((i,k))
    for j in [-1,1]:
        if (D[i+j][k] > D[i][k]) and (D[i+j][k] != 9):
            basin(i+j, k, B)
        if (D[i][k+j] > D[i][k]) and (D[i][k+j] != 9):
            basin(i, k+j, B)
    return len(set(B))

p=1
for i in sorted([basin(l[0], l[1], []) for l in L])[-3:]: p=p*i
print("part 2:", p)

