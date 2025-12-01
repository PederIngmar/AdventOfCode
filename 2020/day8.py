data=[d.split() for d in open("input_day8.txt").read().splitlines()]
Alog=[]
def loop(idx,a,Lidxlog,r):
    global Gidxlog
    global Alog
    while idx < len(data):
        if data[idx][0] == "acc":
            a+=int(data[idx][1])
            idx+=1
        elif data[idx][0] == "jmp":
            idx+=int(data[idx][1])
        else:
            idx+=1
        Lidxlog.append(idx)
        Alog.append(a)
        if len(Lidxlog) != len(set(Lidxlog)):
            if r==0:
                Gidxlog = Lidxlog
                return "part 1:", a
            else:
                return "infinite loop"
    return("part 2:", a)

print(loop(0,0,[0],0))
for i in range(len(Gidxlog)):
    if data[Gidxlog[i]][0] == "jmp":
        print(loop(Gidxlog[i]+1,Alog[i],Gidxlog[:i],1))
    if data[Gidxlog[i]][0] == "nop":
        print(loop(Gidxlog[i]+int(data[Gidxlog[i]][1]),Alog[i],Gidxlog[:i],1))
