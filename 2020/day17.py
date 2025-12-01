data=[list(d) for d in open("input_day17.txt").read().splitlines()]

P = []
P2 = []
for y,Y in enumerate(data):
    for x,X in enumerate(Y):
        if X == "#": 
            P.append((x,y,0))
            P2.append((x,y,0,0))


def f(x,y,z):
    L = [(x+a,y+b,z+c) for a in range(-1,2) for b in range(-1,2) for c in range(-1,2)]
    L.pop(13)
    return len([i for i in L if i in P])

P1 = [i for i in P]

for k in range(2,8):
    for x in range(0-k,7+k):
        for y in range(0-k,7+k):
            for z in range(0-k,0+k):
                c = f(x,y,z)
                if (x,y,z) in P:
                    if c != 2 and c != 3:
                        P1.pop(P1.index((x,y,z)))
                else:
                    if c == 3:                 
                        P1.append((x,y,z))
    P = [i for i in P1]

print("part 1:", len(P))

D, D1 = dict(), dict()
for x in range(-8,15):
    for y in range(-8,15):
        for z in range(-8,8):
            for w in range(-8,8):
                if (x,y,z,w) in P2:
                    D[(x,y,z,w)] = "#"
                    D1[(x,y,z,w)] = "#"
                else:
                     D[(x,y,z,w)] = "."
                     D1[(x,y,z,w)] = "."

def f2(x,y,z,w):
    L = [(x+a,y+b,z+c,w+d) for a in range(-1,2) for b in range(-1,2) for c in range(-1,2) for d in range(-1,2)]
    L.pop(40)
    return len([i for i in L if D[i] == "#"])

for k in range(2,8):
    for x in range(0-k,7+k):
        for y in range(0-k,7+k):
            for z in range(0-k,0+k):
                for w in range(0-k,0+k):
                    c = f2(x,y,z,w)
                    if D[(x,y,z,w)] == "#":
                        if c != 2 and c != 3:
                            D1[(x,y,z,w)] = "."
                    else:
                        if c == 3:                 
                            D1[(x,y,z,w)] = "#"
    for i in D1: D[i] = D1[i]

print("part 2:", len([d for d in D if D[d] == "#"]))
