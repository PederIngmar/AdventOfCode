data=open("input_day6.txt").read().splitlines()
data.append("")
d1=[]
l1,l2=0,0
for d in data:
    if d == "":
        l1+=len(set("".join(d1)))
        y=set(d1[0])
        for i in d1: y=y.intersection(i)
        l2+=len(y)
        d1=[]
    else:
        d1.append("".join(sorted(d)))
print("part 1:",l1," part 2:",l2)