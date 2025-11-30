with open("day10_input.txt") as file:
    data = file.read().splitlines()

cycles = [20, 60, 100, 140, 180, 220, 243]
grid = [["." for i in range(40)] for j in range(6)]

tot = 0
c = 0
X = 1
for d in data:
    if c%40 in [X-1, X, X+1]:
        grid[c//40][c%40] = "#"
    if d[:4] == "noop":
        c += 1
    else:
        c+=1
        if c%40 in [X-1, X, X+1]:
            grid[c//40][c%40] = "#"
        X += int(d[5:])
        c+=1
        
    if c >= cycles[0]-2:
        tot += cycles[0] * X
        cycles.pop(0)
    
print("part 1: ", tot)
print("part 2: ")
for g in grid: print("".join(g))