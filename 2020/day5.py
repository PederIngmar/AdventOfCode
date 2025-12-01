data = open("input_day5.txt").read().splitlines()
ID=[]
for D in data:
    rBlim,rFlim,cRlim,cLlim=127,0,7,0
    for d in D:
        if d=="B":
            rFlim=int((rFlim+rBlim)/2)
        if d=="F":
            rBlim=int((rFlim+rBlim)/2)
        if d=="R":
            cLlim=int((cRlim+cLlim)/2)
        if d=="L":
            cRlim=int((cRlim+cLlim)/2)
    ID.append(rBlim*8 + cRlim)
print("part 1:", sorted(ID)[-1])  
print("part 2:", ([item for item in range(sorted(ID)[0],sorted(ID)[-1]) if item not in ID])[0])