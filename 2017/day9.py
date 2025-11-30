# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:35:48 2019

@author: peder1403
"""

data = str(open("day9_input.txt").read())

D1 = list(data)
D1.pop(-1)
D2 = []
i = 0
while i < len(D1):
    if D1[i] == "!":
        i += 2
    else:
        D2.append(D1[i])
        i += 1
D1 = []
k = 0
u = 0
while k < len(D2):
    if D2[k] == "<":
        u -= 1
        k2 = 0
        while D2[k+k2] != ">":
           k += 1
           u += 1
        k += 1
    else:
        D1.append(D2[k])
        k += 1
D2 = []
for j in range(len(D1)):
    if D1[j] != ",":
        D2.append(D1[j])

print("".join(D2))

level = 0
points = 0
for i in range(len(D2)):
    if D2[i] == "{":
        level += 1
    if D2[i] == "}":
        points += level
        level -= 1
        
        
print("part 1:", points)       
print("part 2:", u)  
