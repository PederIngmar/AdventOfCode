import numpy as np

with open("day1_input.txt") as file:
    data = file.read().splitlines()

data = [[d[0], int(d[1:])] for d in data]

sum = 50
code = 0
for d in data:
    if d[0] == "R":
        sum += d[1]
    elif d[0] == "L":
        sum -= d[1]
    sum = sum%100
    if sum == 0:
        code += 1

print("part 1: ", code)

sum = 50
code = 0
for dir, val in data:
    atzero = 1
    if sum == 0:
        atzero = 0

    if dir == "R":
        sum += val
        if sum >= 100:
            code += sum // 100

    elif dir == "L":
        sum -= val
        if sum <= 0:
            code += atzero + abs(sum) // 100

    sum = sum%100
    
print("part 2: ", code)
