data = [int(i) for i in open("day6_input.txt").read().split(",")]

#algorithem for part 1:

D = data.copy()
D1=[]
for i in range(80):
    for d in D:
        if d == 0:
            D1.append(6)
            D1.append(8)
        else:
            D1.append(d-1)
    D = D1.copy() 
    D1.clear()
print("part 1:", len(D))


#algorithem for part 2:

def bintre(dager, c):
    if dager-(6+1) >= 0:
        if B[0][dager] == 0:
            B[0][dager] = bintre(dager-(6+1), 0)
        c += B[0][dager]
    else:
        c+=1
    if dager-(8+1) >= 0:
        if B[1][dager] == 0:
            B[1][dager] = bintre(dager-(8+1), 0)
        c += B[1][dager]
    else:
        c+=1
    return c

B = [[0 for dager in range(1,256)] for i in range(2)]
L = [] 
for i in range(1, 6):
    L.append(bintre(256-(i+1), 0))

C=0
for d in data:
    C+=L[d-1]
print("part 2:", C)
