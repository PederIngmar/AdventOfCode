data=[(d[0],int(d[1:])) for d in open("input_day12.txt").read().splitlines()]

x,y,r = 0,0,90
for i in data:
    r = r%360
    if i[0] == "N":
        y += i[1]
    if i[0] == "S":
        y -= i[1]
    if i[0] == "E":
        x += i[1]
    if i[0] == "W":
        x -= i[1]
    if i[0] == "F":
        if r == 0:
            y += i[1]
        if r == 180:
            y -= i[1]
        if r == 90:
            x += i[1]
        if r == 270:
            x -= i[1]
    if i[0] == "R":
        r += i[1]
    if i[0] == "L":
        r-= i[1]

print("part 1:",abs(x)+abs(y))

x, y, wx, wy = 0, 0, 10, 1
for j,i in enumerate(data):
    r=0
    if i[0] == "N":
        wy += i[1]
    if i[0] == "S":
        wy -= i[1]
    if i[0] == "E":
        wx += i[1]
    if i[0] == "W":
        wx -= i[1]
    if i[0] == "F":
        x += wx * i[1]
        y += wy * i[1]


    if i[0] == "R":
        r = i[1]%360
    if i[0] == "L":
        r = -i[1]%360

    if r == 180:
        wx, wy = -wx, -wy
    if r == 90:
        wx, wy = wy,-wx
    if r == 270:
        wx, wy = -wy, wx

print("part 2:",abs(x)+abs(y))