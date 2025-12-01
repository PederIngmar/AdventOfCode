data = [d.split(" ") for d in open("day2_input.txt").read().splitlines()]

def tell(r):
    c=0
    for d in data:
        if d[0] == r:
            c+=int(d[1])
    return c

print("part 1:", (tell("down")-tell("up"))*tell("forward"))

aim = 0
depth = 0
pos = 0
for d in data:
    if d[0] == "down":
        aim += int(d[1])
    if d[0] == "up":
        aim -= int(d[1])
    if d[0] == "forward":
        pos += int(d[1])
        depth += int(d[1])*aim

print("part 2:", depth*pos)