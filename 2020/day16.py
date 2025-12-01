data = open("input_day16.txt").read().splitlines()
#print(open("input_day16.txt").read())
IN = [[i[:i.index(":")], list(map(int,i[i.index(":")+2 : i.index("or ")-1].split("-"))), list(map(int,i[i.index("or ")+3:].split("-")))] for i in data[:20]]
mt = [int(i) for i in data[22].split(",")]
NT = [[int(k) for k in i.split(",")] for i in data[25:]]

IV, V = [],[]
for a in NT:
    v = 0
    for b in a:
        iv = 0
        for i in IN:
            if (b >= i[1][0] and b <= i[1][1]) or (b >= i[2][0] and b <= i[2][1]):
                pass
            else:
                iv += 1
        if iv == len(IN):
            IV.append(b)
        else:
            v += 1
    if v == len(a):
        V.append(a)

print("part 1:",sum(IV))

D = dict()
for c in range(20): D[c] = []
for r in range(len(V[0])):
    for i in IN:
        a = 0
        for c in range(len(V)):
            if (V[c][r] >= i[1][0] and V[c][r] <= i[1][1]) or (V[c][r] >= i[2][0] and V[c][r] <= i[2][1]):
                a += 1  
        if a == len(V):
            D[r].append(i[0])
L = []
for a in IN:
    L.append(([b for a in D.values() for b in a].count(a[0]),a[0]))

for l in sorted(L):
    for i in D:
        for k in D[i]:
            if k == l[1]:
               D[i] = l[1]
m = 1
for i in D:
    if "departure" in D[i]:
        m = m * mt[i]
print("part 2:",m)