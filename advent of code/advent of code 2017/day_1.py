# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:20:44 2019

@author: peder1403
"""

data = open("day1_input.txt").readlines()


K = [int(i) for i in str(data[0])]

sumlist = []
for i in range(len(K)-1):
    v1=K[i]
    v2=K[i+1]
    if v1 == v2:
        sumlist.append(v1)

print("del 1:" , sum(sumlist)+1) # +1 fordi listen er en sirkel som starter og slutter med 1


###part2###
L = [int(i) for i in str(data[0])]

sumlist = []
for i in range(len(L)):
    if i >= len(L)/2:
        v1=K[i]
        v2=K[i - int(len(L)/2)]
    else:
        v1=K[i]
        v2=K[i+ int(len(L)/2)]
    if v1 == v2:
        sumlist.append(v1)

print("del 2:" , sum(sumlist))
