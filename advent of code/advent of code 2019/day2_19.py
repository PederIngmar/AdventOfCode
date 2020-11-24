# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:58:08 2019

@author: peder1403
"""

data = open("input_day2_19.txt").read().strip("\n").split(",")
data = list(map(int,data))
data0 = list(data)

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

print("part 1:", alg(12,2))

for n in range(100):
    for v in range(100):
        if alg(n,v) == 19690720:
            print("part 2:", (100*n)+v)