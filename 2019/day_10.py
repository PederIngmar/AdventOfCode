# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:05:06 2020

@author: peder1403
"""
import math
data = open("input_day10.txt").read().splitlines()
#print(data)

cords=[]
for l in range(len(data)):
    for i in range(len(data[l])):
        if data[l][i] == "#":
            cords.append((i,l))
#print(cords)

def retningsvektor(cord1,cord2):
    v = (cord2[0]-cord1[0], cord2[1]-cord1[1])
    if v[0]+v[1] == 0:
        return v
    elif (v[0]==0):
        return (0, v[1]/abs(v[1]))
    elif (v[1]==0):
        return (v[0]/abs(v[0]),0)
    
    else:
        v = (v[0]/v[0], v[1]/v[0])
        return v

m=0

for cord1 in cords:
    rv = []
    for cord2 in cords:
        rv.append(retningsvektor(cord1,cord2))
    if len(set(rv)) > m:
        m = len(set(rv))
        C=cord1

def findangle(c1):
    c1 = (c1[0]-C[0], c1[1]-C[1])
    
    cv = c1[1]/math.sqrt(c1[0]^2 + c1[1]^2)
    print(cv)
    return math.degrees(math.acos(cv))
    
    
print(C)
cords.pop(cords.index(C))

print(findangle((1,1)))
