data = [1,17,0,10,18,11,6]
def f(l):
    D = dict()
    for i, I in enumerate(data): D[I] = i
    n = 0
    for i in range(len(data),l-1):
        if n in D.keys():
            D[n], n = i, i - D[n]
        else:
            D[n], n = i, 0
    return n

print("part 1:", f(2020))
print("part 2:", f(30000000))