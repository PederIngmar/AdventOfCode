data = open("day4_input.txt").read().split("\n\n")
#print(data)
N = list(map(int ,data[0].split(",")))
D = {i:[] for i in range(100)}
RC = dict()
L=[]
for bord in range(len(data[1:])):
    L1 = []
    for row in range(5):
        R = data[1:][bord].split("\n")[row].split(" ")
        L2 = []
        RC[(bord,row,"")] = 0
        for column in range(len(R)):
            if R[column] != "":
                L2.append(int(R[column]))
        for l2 in range(5):
            RC[(bord,"",l2)] = 0
            D[int(L2[l2])].append([bord, row, l2, 0]) 

        L1.append(L2)
    L.append(L1)


def bingo():
    for n in N:
        for i in range(len(D[n])):
            D[n][i][3] = 1
            RC[(D[n][i][0],D[n][i][1],"")] += 1
            RC[(D[n][i][0],"",D[n][i][2])] += 1
            if (RC[(D[n][i][0],D[n][i][1],"")] == 5) or (RC[(D[n][i][0],"",D[n][i][2])] == 5):
                s=0
                for l in L[D[n][i][0]]:
                    for j in l:
                        if (D[j][0][3] == 0):
                            s+=j
                return(n*s)

def bingo2():
    B =list(range(100))
    for n in N:
        for i in range(len(D2[n])):
            D2[n][i][3] = 1
            RC2[(D2[n][i][0],D2[n][i][1],"")] += 1
            RC2[(D2[n][i][0],"",D2[n][i][2])] += 1
            if (RC2[(D2[n][i][0],D2[n][i][1],"")] == 5) or (RC2[(D2[n][i][0],"",D2[n][i][2])] == 5):
                B[D2[n][i][0]] = -1
                if sum(B) == -100:
                    s=0
                    for l in L[D2[n][i][0]]:
                        for j in l:
                            if (D2[j][0][3] == 0):
                                s+=j
                    return(n*s)

D2 = D.copy()
RC2 = RC.copy()

print("part 1:", bingo())
print("part 2:", bingo2())
