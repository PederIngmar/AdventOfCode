data = [[[set(k) for k in j.split(" ")] for j in i.split(" | ")] for i in open("day8_input.txt").read().splitlines()]
c=0
for d in data:
    for i in d[1]:
        if len(i) in [2, 4, 3, 7]:#1 4 7 8
            c+=1
print("part 1:", c)

c=0
for d in data:
    D = dict()
    D[1] = [i for i in d[0] if len(i) == 2][0]
    D[4] = [i for i in d[0] if len(i) == 4][0]
    D[7] = [i for i in d[0] if len(i) == 3][0]
    D[8] = [i for i in d[0] if len(i) == 7][0]
    for l in [i for i in d[0] if len(i) == 6]:
        if len(l-D[4]) == 2:
            D[9] = l
        elif len(l-D[1]) == 5:
            D[6] = l
        else:
            D[0] = l

    for l in [i for i in d[0] if len(i) == 5]:
        if len(l-D[4]) == 3:
            D[2]=l
        elif len(l-D[1]) == 3:
             D[3] = l
        else:
             D[5] = l
    
    n = ""
    for i in d[1]:
        for j in D:
            if D[j] == i:
                n+=str(j)
                break
    c+=int(n)
print("part 2:", c)