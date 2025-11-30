with open("day11_input.txt") as file:
    data = [i.splitlines() for i in file.read().split("\n\n")]

items = [[int(i) for i in d[1][d[1].index(":")+1:].split(",")] for d in data]
operations = [d[2][23:] for d in data]
test = [int(d[3].split(" ")[-1]) for d in data]
true = [int(d[4][-1]) for d in data]
false = [int(d[5][-1]) for d in data]
inspections = [0 for i in range(len(data))]

factor = 1
for t in test: factor*=t


for r in range(10000):
    for m in range(len(items)):
        for i in range(len(items[m])):
            old = items[m][i]
            throw_item = eval("old" + operations[m])%factor 
            if throw_item%test[m] == 0:
                items[true[m]].append(throw_item)
            else:
                items[false[m]].append(throw_item)
        inspections[m] += len(items[m])
        items[m] = []
        
inspections.sort()
print("part 2:", inspections[-1]*inspections[-2])
