print("part 1:", len([d for d in [sorted([int(a.strip()) for a in d.split("  ")[1:] if a != ""]) for d in open("input_day3.txt").read().splitlines()] if d[0]+d[1]>d[2]]))
D = [d for d in [[int(a.strip()) for a in d.split("  ")[1:] if a != ""] for d in open("input_day3.txt").read().splitlines()]]

D2=[]
for i in range(0,int(len(D)),3):
    D2.append(sorted([D[i][0],D[i+1][0],D[i+2][0]]))
    D2.append(sorted([D[i][1],D[i+1][1],D[i+2][1]]))
    D2.append(sorted([D[i][2],D[i+1][2],D[i+2][2]]))
s=0
for d in D2:
    if d[0]+d[1]>d[2]:
        s+=1
print("part 2:", s)
print(len(D),len(D2))
