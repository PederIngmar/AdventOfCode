with open("day11_input.txt") as file:
    data = [i.splitlines() for i in file.read().split("\n\n")]
monkeys = len(data)
items = []
owner_item = []
for d in range(monkeys):
    t = [int(i) for i in data[d][1][data[d][1].index(":")+1:].split(",")]
    items += t
    owner_item += [d]*len(t)

operations = [d[2][23:] for d in data]
test = [int(d[3].split(" ")[-1]) for d in data]
true = [int(d[4][-1]) for d in data]
false = [int(d[5][-1]) for d in data]
inspections = [0 for i in range(monkeys)]

for r in range(20):
    for m in range(monkeys):
        for o in range(len(owner_item)):
            if owner_item[o] == m:
                old = items[o]
                old = eval("old" + operations[m])
                old = int(old/3)
                if old%test[m] == 0:
                    owner_item[o] = true[m]
                else:
                    owner_item[o] = false[m]
                items[o] = old
                inspections[m] += 1
        
inspections.sort()
print("part 1:", inspections[-1]*inspections[-2])