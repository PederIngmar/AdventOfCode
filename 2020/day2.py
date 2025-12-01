data=[d.replace("-"," ").replace(":","").split() for d in open("input_day2.txt").read().splitlines()]
c1, c2 = 0,0
for d in data:
    if int(d[0])<=d[3].count(d[2])<=int(d[1]):
        c1+=1
    if (d[3][int(d[0])-1] == d[2] or d[3][int(d[1])-1] == d[2]) and not (d[3][int(d[0])-1] == d[2] and d[3][int(d[1])-1] == d[2]):
        c2+=1

print("part 1:",c1,"part2:", c2)
