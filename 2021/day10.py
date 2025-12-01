data = open("day10_input.txt").read().splitlines()

B = {"(":")","[":"]","{":"}","<":">"}
P = {")": 3,"]": 57,"}": 1197,">": 25137}
P2 = {")": 1,"]": 2,"}": 3,">": 4}
S = []
c = 0
for d in data:
    f = True
    L = []
    for i in d:
        if i in B:
            L.append(i)
        elif B[L[-1]] == i:
            L.pop(-1)
        else:
            f = False
            L.pop(-1)
            c+=P[i]
    if f:
        s = 0
        for k in [P2[B[L[-i-1]]] for i in range(len(L))]:
            s = s*5 + k
        S.append(s)

print("part 1:", c)
print("part 2:", sorted(S)[int(len(S)/2)])
