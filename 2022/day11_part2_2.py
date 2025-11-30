with open("day11_input.txt") as file:
    data = [i.splitlines() for i in file.read().split("\n\n")]

operations = [d[2][23:].split(" ") for d in data]
test = [int(d[3].split(" ")[-1]) for d in data]
true = [int(d[4][-1]) for d in data]
false = [int(d[5][-1]) for d in data]
inspections = [0 for i in range(len(data))]
items = [[[i%j for j in test] for i in [int(i) for i in d[1][d[1].index(":")+1:].split(",")]] for d in data]
print(test)
print(items)
def operat(op, L):
    if op[1] != "old":
        if op[0] == "*":
            return [(I*int(op[1]))%test[i] for i,I in enumerate(L)]
        else:
            return [(I+int(op[1]))%test[i] for i,I in enumerate(L)]
    else:
        return [(I*I)%test[i] for i,I in enumerate(L)]
        #return L
log = []
for r in range(3):
    for m in range(len(items)):
        for i in range(len(items[m])):
            throw_item = operat(operations[m], items[m][i])
            #print(operations[m], items[m][i], test)
            #print("----")
            #print(throw_item)
            #print("-----------------")
            if items[m][i][m] == 0:
                items[true[m]].append(throw_item)
                log.append(true[m])
            else:
                items[false[m]].append(throw_item)
                log.append(false[m])
        inspections[m] += len(items[m])
        items[m] = []

#print(len(items))
inspections.sort()
#print(inspections)
#print(log)
print("part 2:", inspections[-1]*inspections[-2])
#57354
