# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 00:19:51 2019

@author: peder1403
"""

data = open("input_day5_19.txt").read().strip("\n").split(",")
data = list(map(int,data))
data0 = list(data)



T = True
k=0
outputs = []
while T == True:
    print("###########")
    G = map(int, list(str(data[k])))
    G = list(G)

    mode1 = 0
    mode2 = 0
    try:
        G.pop(-2)
    except IndexError:
        pass
    
    opcode = G[-1]
    print(opcode)
    print(data[k+1],data[k+2],data[k+3])
    try:
        mode1 = G[-2]
    except IndexError:
        pass
    
    try:
        mode2 = G[-3]
    except IndexError:
        pass
    
    if opcode == 9:
            T = False
    elif opcode == 4:
        outputs.append(data[data[k+1]])

        print(outputs)
        k+=2
    else:
        if mode1 == 0:
            p1 = data[data[k+1]]
        elif mode1 == 1:
            p1 = data[k+1]
        
        if mode2 == 0:
            p2 = data[data[k+2]]
        elif mode2 == 1:
            p2 = data[k+2]
        if opcode == 5:
            if data[k+1] != 0:
                k = data[k+2]
            else:
                k+=4
        if opcode == 6:
            if data[k+1] == 0:
                 k = data[k+2]
            else:
                k+=4
        if opcode == 7:
            if data[k+1]<data[k+2]:
                data[data[k+3]] = 1
            else:
                data[data[k+3]] = 0
        if opcode == 8:
            if data[k+1] == data[k+2]:
                data[data[k+3]] = 1
            else:
                data[data[k+3]] = 0
        if opcode == 1:
            data[data[k+3]] = p1 + p2
            k+=4
            
        if opcode == 2:
            data[data[k+3]] = p1 * p2
            k+=4
        if opcode == 3:
            data[data[k+1]] = 5
            k+=2
    
        
    #print(k)
print(outputs)

"""
def alg(noun, verb):
    data = list(data0)
    data[1] = noun
    data[2] = verb
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        if data[i] == 2:
            #print(i)
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        if data[i] == 99:
            #print(i)
            break
        if (data[i] != 1) and (data[i] != 2) and (data[i] != 99):
            print("error", i, data[i])
    return data[0]
"""