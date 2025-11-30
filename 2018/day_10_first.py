# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:48:50 2019

@author: peder1403
"""
import matplotlib.pyplot as plt

data = open("day_10_input.txt").readlines()

D = []
for i in data:
    st = i.find("position") + len("position") + 2
    slt  = i.find(",")
    x = i[st:slt]
    
    st = slt + 1
    slt = i.find(">")
    y = i[st:slt]
    
    st = i.find("velocity") + len("velocity") + 2
    slt  = st + 2
    vx = i[st:slt]
    
    st = slt + 1
    slt = len(i)-2
    vy = i[st:slt]
    
    D.append([int(x), int(y), int(vx), int(vy)])

X = 7

for T in range(10209, 10631, 1):
    D2 = [ [i[0]+T*i[2], i[1]+T*i[3], i[2], i[3]] for i in D]
    dist = 0
    for i in D2:
        dist +=  abs(D2[0][0] - i[0]) + abs(D2[0][1] - i[1])
    if dist < 16100:
        print(T,":",dist)
        plt.plot([x[0] for x in D2], [x[1] for x in D2], "g*")
        plt.xlim(160, 280)
        plt.ylim(200, 100) #opp ned
        plt.savefig("day_10_fig" + str(T) + ".png")
        plt.close()
