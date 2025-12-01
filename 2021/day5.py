import math
data = [[[int(c) for c in b.split(",")] for b in a.split(" -> ")] for a in open("day5_input.txt").read().splitlines()]
P = []
P2 = []
for d in data:
    dx= d[1][0]-d[0][0]
    dy= d[1][1]-d[0][1]
    if (dx == 0):
        for i in range(0, dy+int(dy/abs(dy)), int(dy/abs(dy))):
            P.append((d[0][0], d[0][1]+i))
            P2.append((d[0][0], d[0][1]+i))
    elif (dy == 0):
        for i in range(0, dx+int(dx/abs(dx)), int(dx/abs(dx))):
            P.append((d[0][0]+i, d[0][1]))
            P2.append((d[0][0]+i, d[0][1]))
    else:
        for i, j in zip(range(0, dx+int(dx/abs(dx)), int(dx/abs(dx))), range(0, dy+int(dy/abs(dy)), int(dy/abs(dy)))):
            P2.append((d[0][0]+i, d[0][1]+j))

def count(L):
    L.sort()
    c=0
    flag = False
    for l in range(1, len(L)):
        if L[l] == L[l-1]:
            if flag == False:
                c+=1
            flag=True
        else:
            flag = False
    return c

print("part 1:", count(P))
print("part 2:", count(P2))