data = open("input_day19.txt").read().splitlines()

D = dict()
for a in data[:133]:
    D[int(a[:a.index(":")])] = [i.split(" ") for i in a[a.index(":")+2:].split(" | ")]

#print([[[int(a) for a in b] for b in d] for d in D.values()])

#print(D)
codes = data[134:]

