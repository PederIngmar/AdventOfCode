data = list(map(int,open("input_day9.txt").read().splitlines()))
#print(data)

for i in range(25, len(data)):
    pre = data[i-25:i]
    c=0
    for a in pre:
        for b in pre:
            if (a != b) and (a+b==data[i]):
                c+=1
    if c == 0:
        n = data[i]
        break

print("part 1:", n)

for a in range(len(data)):
    for l in range(2, 20):
        L=data[a:a+l]
        if sum(L) == n:
            print("part 2:", min(L)+max(L))
            break