data = [list(d) for d in open("input_day11.txt").read().splitlines()]
#print(data)
D = [[i for i in d] for d in data]
Dn = [["." for i in d] for d in data]

def s(x,y):
    L=[(x+a,y+b) for a in range(-1,2) for b in range(-1,2) if ((x+a,y+b) != (x,y)) and (x+a >= 0) and (x+a < len(D[0])) and (y+b >= 0) and (y+b < len(D))]
    return L


j = 0
while j < len(D)*len(D[0]):
    j = 0
    for y, Y in enumerate(D):
        for x, X in enumerate(Y):

            c = len([i for i in s(x,y) if D[i[1]][i[0]] == "#"])
            if D[y][x] == "L" and c == 0:
                Dn[y][x] = "#"

            elif D[y][x] == "#" and c >= 4:
                Dn[y][x] = "L"

            else:
                j+=1
    D = [[i for i in d] for d in Dn]

print("part 1:", len([b for a in D for b in a if b == "#"]))

D = [[i for i in d] for d in data]
Dn = [[i for i in d] for d in data]

def s2(x,y,a,b):
    a1, b1 = a, b
    while (x+a1 < len(D[0])) and (y+b1 < len(D)) and (x+a1 >= 0) and (y+b1 >= 0):
        if D[y+b1][x+a1] == "#":
            return 1
        if D[y+b1][x+a1] == "L":
            return 0
        a1,b1 = a1+a, b1+b
    return 0

j = 0
while j < len(D)*len(D[0]):
    j = 0
    for y, Y in enumerate(D):
        for x, X in enumerate(Y):
            c2 = sum([s2(x,y,a,b) for a in range(-1,2) for b in range(-1,2) if ((x+a,y+b) != (x,y))])

            if D[y][x] == "L" and c2 == 0:
                Dn[y][x] = "#"

            elif D[y][x] == "#" and c2 >= 5:
                Dn[y][x] = "L"

            else:
                j+=1

    D = [[i for i in d] for d in Dn]

print("part 2:",len([b for a in D for b in a if b == "#"]))