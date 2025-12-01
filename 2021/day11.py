data = open("day11_input.txt").read().splitlines()
D = [[0 for x in range(len(data[0])+2)] for y in range(len(data)+2)]
for y in range(len(data)):
    for x in range(len(data[0])):
        D[y+1][x+1] = int(data[y][x])

def flash(y, x):
    global f
    f+=1
    D[y][x] = 0
    for b in range(-1, 2):
        for a in range(-1, 2):
            if D[y+b][x+a] != 0:
                D[y+b][x+a] += 1
                if D[y+b][x+a] > 9:
                    flash(y+b,x+a)

f=0
c = 0
while sum([sum(a) for a in D]) != 0:
    for y in range(len(data)):
        for x in range(len(data[0])):
            D[y+1][x+1] += 1

    for y in range(len(data)):
        for x in range(len(data[0])):
            if D[y+1][x+1] > 9:
                flash(y+1,x+1)
    c+=1
    if c == 100:
        print("part 1:", f)
print("part 2:", c)
