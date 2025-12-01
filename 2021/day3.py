data = open("day3_input.txt").read().splitlines()
#print(data)
gamma = ""
epsilon = ""
for i in range(12):
    a0,a1 = 0,0
    for d in data:
        if d[i] == "1":
            a1+=1
        else:
            a0+=1
    if a0>a1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
print("part 1:", int(gamma, 2)*int(epsilon, 2))


C = data.copy()
i=0
while len(C) > 1:
    L1 = []
    L0 = []
    for d in C:
        if d[i] == "1":
            L1.append(d)
        else:
            L0.append(d)
    if len(L0)<=len(L1):
        C = L0
    else:
        C = L1
    i+=1


O = data.copy()
i=0
while len(O) > 1:
    L1 = []
    L0 = []
    for d in O:
        if d[i] == "1":
            L1.append(d)
        else:
            L0.append(d)
    if len(L1)>=len(L0):
        O = L1
    else:
        O = L0
    i+=1

print("part 2:", int(O[0],2)*int(C[0],2))