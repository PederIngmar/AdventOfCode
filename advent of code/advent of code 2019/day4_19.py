# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:44:28 2019

@author: peder1403
"""

input = [108457, 562041]


L = []
nL = []
for i in range(input[0], input[1], 1):
    l = list(str(i))
    if (l[0]<=l[1]<=l[2]<=l[3]<=l[4]<=l[5]):
        for k in l:
            if (l.count(k) == 2):
                L.append(int("".join(l)))
            if (l.count(k) > 1):
                nL.append(int("".join(l)))
                
nL = set(nL)
L = set(L)     
print("part 1:", len(nL))
print("part 2:", len(L))

