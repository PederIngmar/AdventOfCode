with open("day12_input.txt") as file:
    data = [[j if j.isupper() else ord(j)-96 for j in list(i.lower())] for i in file.read().splitlines()]
print(data[20])
#for d in data: print(d)
