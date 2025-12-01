data = sorted(list(map(int,open("input_day10.txt").read().splitlines())))
data.append(max(data)+3)
data.insert(0,0)

n,L=0,[]
for i in data:
    L.append(i-n)
    n=i
print("part 1:", (L.count(3))*L.count(1))

P={0:1}
for i in range(1, len(data)):
    P[i]=0
    j=1
    while (data[i-j] >= data[i]-3) and (i-j >= 0):
        P[i]+=P[i-j]
        j+=1

print("part 2:", P[len(data)-1])