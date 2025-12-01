import string
data = [d.strip("\n").replace("[","-").replace("]","").split("-") for d in open("input_day4.txt", "r").read().splitlines()]
c=0
for d in data:
    D=[]
    s="".join(sorted("".join([e for e in d[:-2]])))
    for j in range(len(d[-1])):
        m=0
        for i in sorted(list(set(list(s)))):
            if s.count(i)>m: 
                m=s.count(i)
                sm=i
        s=s.replace(sm,"")
        D.append(sm)
    if D==list(d[-1]):
        c+=int(d[-2])
print("part 1:", c)

alph=list(string.ascii_lowercase)

#print(alph[25%len(alph)])
for d in data:
    code=""
    L="".join([(e+" ") for e in d[:-2]])
    for l in L:
        if l != " ":
            code+=alph[(int(d[-2])+alph.index(l))%(len(alph))]
        else:
            code+=" "
    if code == "northpole object storage ":
        print ("part 2:", d[-2])
        break
