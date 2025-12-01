data = list(map(int, open("day1_input.txt").read().splitlines()))
c1=0
for d in range(len(data)-1):
    if data[d+1]>data[d]:
        c1+=1     
print("part 1:", c1)

c2 = 0
for d in range(len(data)-3):
    if (data[d+3]+data[d+2]+data[d+1]) > (data[d]+data[d+1]+data[d+2]):
        c2+=1
    
print("part 2:", c2)