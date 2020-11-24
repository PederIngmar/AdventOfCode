# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:20:17 2019

@author: peder1403
"""

checksum = 0

data = open("day2_input.txt").readlines()

dif = 0
for line in data:
    L = [int(s) for s in line.split() if s.isdigit()]
    L.sort()
    dif += int(L[-1]) - int(L[0])
print("part 1:", dif)

###part2###

s = 0
for line in data:
    L = [int(s) for s in line.split() if s.isdigit()]
    L.sort()
    #print(L)
    for i in range(len(L)):
        l1 = L[-i]
        for k in range(len(L)-i):
            l2 = L[-(i+k+1)]
            d = l1/l2
            if (d).is_integer() and d != 1:
                #print(l1, l2)
                #print(d)
                s += d
print("part 2:", int(s))