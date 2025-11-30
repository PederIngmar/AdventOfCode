with open("day4_input.txt") as data:
    D = [[[int(h) for h in j.split("-")] for j in i.split(",")] for i in data.read().splitlines()]

c = 0
c2 = 0
for d in D:
    a = d[0][0] >= d[1][0]
    b = d[0][1] <= d[1][1]
    a1 = d[0][0] <= d[1][0]
    b1 = d[0][1] >= d[1][1]
    c += ((a and b) or (a1 and b1))
    c2 += len(set(range(d[0][0], d[0][1]+1))&set(range(d[1][0], d[1][1]+1))) > 0

print(f"part 1: {c}")
print(f"part 2: {c2}")