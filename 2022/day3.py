with open("day3_input.txt") as file:
    data = file.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

S = 0
for d in data:
    c = list(set(d[:int(len(d)/2)])&set(d[int(len(d)/2):]))[0]
    S += alphabet.index(c)+1
print("part 1: ", S)

S = 0
for i in range(0, len(data), 3):
    c = list(set(data[i])&set(data[i+1])&set(data[i+2]))[0]
    S += alphabet.index(c)+1
print("part 2: ", S)
