import itertools

data = open("input_day14.txt").read().splitlines()
data.append("mask")
D,d1=[],[]
for d in data:
    if d[:4] == "mask":
        D.append(d1)
        d1 = [d[7:]]
    else:
        d1.append((int(d[d.index("[")+1:d.index("]")]), int(d[d.index("=")+2:])))

def s(b):
    c = list(itertools.product([0,1],repeat=b.count("X")))
    L=[]
    for i in c:
        I = []
        j = 0
        for k in b:
            if k == "X":
                I.append(str(i[j]))
                j+=1
            else:
                I.append(str(k))
        L.append(int("".join(I),2))
    return L

L1 = dict()
L2 = dict()
for d in D:
    for i in d[1:]:
        a = list("0" * (36-len('{0:08b}'.format(i[1]))) +'{0:08b}'.format(i[1]))
        b = list("0" * (36-len('{0:08b}'.format(i[0]))) +'{0:08b}'.format(i[0]))
        for k in range(36):
            if d[0][k] != "X" and d[0][k] != a[k]:
                a[k] = d[0][k]
            if d[0][k] != "0":
                b[k] = d[0][k]
            
        L1[i[0]] =  int("".join(a), 2)
        for j in s(b): L2[j] = i[1]
print("part 1:", sum(L1.values()))
print("part 2:", sum(L2.values()))
