import numpy as np
with open("day9_input.txt") as file:
    data = [i.split(" ") for i in file.read().splitlines()]


def plot(L):
    P = [[str(9-L.index((i, 20-j))) if (i, 20-j) in L else "." for i in range(26)] for j in range(21)]
    for p in P:
        print(p)


dir_dict = {"U":np.array([0,1]),"R":np.array([1,0]),"D": np.array([0,-1]),"L":np.array([-1,0])}

logT = [(0,0)]
H = np.array([0,0])
T = np.array([0,0])


for d in data:
    for i in range(int(d[1])):
        orgin = H.copy()
        H += dir_dict[d[0]]
        if (abs(H-T) > np.array([1,1])).any():
            T = orgin
        logT.append(tuple(T))
    
print("part 1: ", len(set(logT)))


movelen_dict = {
(1,2) : (1,1), 
(-1,2) : (-1,1), 
(1,-2) : (1,-1), 
(-1,-2) : (-1,-1),
(2,1) : (1,1),
(2,-1) : (1,-1),
(-2,1) : (-1,1),
(-2,-1) : (-1,-1),
(0,2) : (0,1),  
(0,-2) : (0,-1), 
(2,0) : (1,0),
(-2,0) : (-1,0),
(2,2) : (1, 1),
(2,-2) : (1, -1),
(-2,2) : (-1, 1),
(-2,-2) : (-1, -1)}



logT = [(0,0)]
rope = [np.array([0,0]) for i in range(10)]

for d in data:
    for i in range(int(d[1])):
        rope[0] += dir_dict[d[0]]
        for j in range(1,10):
            if (abs(rope[j]-rope[j-1]) > np.array([1,1])).any():
                rope[j] += movelen_dict[tuple(rope[j-1]-rope[j])]
            else:
                break
        logT.append(tuple(rope[-1]))

print("part 2: ", len(set(logT)))