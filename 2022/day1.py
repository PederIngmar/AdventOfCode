with open("day1_input.txt") as file:
    data = file.read().splitlines()

d1 = 0
D=[]
for d in data:
    if d == "":
        D.append(d1)
        d1=0
    else:
        d1+=int(d)

print("part 1: ", sorted(D)[-1])
print("part 2: ", sum(sorted(D)[-3:])) 
