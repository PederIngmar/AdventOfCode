# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:29:36 2019

@author: peder1403
"""

#data = open("day5_input.txt").read().splitlines()

D = []
for line in open("day5_input.txt").readlines():
    data = int(line)
    D.append(data)

i = 0
step = 0
count = 0
while D[i] + i < len(D):
    step = D[i]
    D[i] += 1
    i += step
    count += 1
    
print("answer_1:",count+1)

D2 = []
for line in open("day5_input.txt").readlines():
    data = int(line)
    D2.append(data)
    
i = 0
step = 0
count = 0
while D2[i] + i < len(D2):
    step = D2[i]
    if D2[i] > 2:
        D2[i] -= 1
    else:
        D2[i] += 1
    i += step
    count += 1
print("answer_2:",count+1)