with open("day8_input.txt") as file:
    data = [[int(i) for i in j] for j in file.read().splitlines()]

c = 0
for a in range(1, len(data)-1):
    for b in range(1, len(data[a])-1):
        right = data[a][b] > max(data[a][b+1:])
        left =  data[a][b] > max(data[a][:b])
        up = data[a][b] > max([data[i][b] for i in range(a+1,len(data))])
        down = data[a][b] > max([data[i][b] for i in range(0,a)])
        if right or left or up or down:
            c += 1
            
border = len(data)*2 + len(data[0])*2 - 4
print("part 1:", c+border)

def find_view(L,start):
    #if len(L) == 0: return 0
    i = 0
    while (i < len(L)-1) and (L[i] < start): 
        i += 1
    return i+1

score_max = 0
for a in range(len(data)):
    for b in range(len(data[a])):
        right = data[a][b+1:]        
        left =  data[a][:b]
        left.reverse()
        up = [data[i][b] for i in range(a+1,len(data))]
        down = [data[i][b] for i in range(0,a)]
        down.reverse()

        start = int(data[a][b])
        score = find_view(right,start) * find_view(left,start) * find_view(up,start) * find_view(down,start)
        if score > score_max:
            score_max = score
print("part 2:", score_max)