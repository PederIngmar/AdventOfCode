data = [d.replace(" bags","").replace(" bag","").replace(" contain",",").replace(".","").replace(",","").split() for d in open("input_day7.txt").read().splitlines()]
D=[]
for d in data:
    if d[2] != "no":
        d1=[]
        d1.append(" ".join([d[0],d[1]]))
        for i in range(2,len(d),3):
            d1.append([int(d[i])," ".join([d[i+1],d[i+2]])])
        D.append(d1)
#print(D)
S=[]
def p1(s):
    for d in D:
        for i in d[1:]:
            if i[1] == s:
                S.append((d[0]))
                p1(d[0])

p1("shiny gold")
print("part 1:", len(set(S)))

def p2(s,v):
    for d in D:
        if d[0] == s:
            for i in d[1:]:
                v += int(i[0]) + int(i[0]) * p2(i[1],0)
    return v
print("part 2:",p2("shiny gold",0))