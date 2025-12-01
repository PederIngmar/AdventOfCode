data = open("input_day13.txt").read().splitlines()
n = int(data[0])
D = data[1].split(",")

L=dict()
L2=[]
for j, d in enumerate(D):
    if d != "x":
        L[[i+int(d) for i in range(0,n, int(d))][-1]] = int(d)
        L2.append((int(d),j))
print( "part 1:", (min(L.keys()) - n) * L[min(L.keys())] )

t,c,j = 0,0,19*823*17*29*37
while c < len(L2):
    c = 0
    for d in L2:
        if (t + d[1] - 19) % d[0] == 0:
            c+=1
        else:
            t+=j
            break

print("part 2:", t-19, "   (not a general solution!)")