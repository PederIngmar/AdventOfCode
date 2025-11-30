# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:56:07 2019

@author: peder1403
"""

data = open("day8_input.txt").read().splitlines()

D = []
for line in data:
    k = list(line.split())
    D.append(k)
    
nameset = set()
for k in range(len(D)):
    nameset.add(D[k][4])
    nameset.add(D[k][0])

namelist = tuple(nameset)
valuelist = [0 for i in range(len(nameset))]

log = set()
for k in range(len(D)):
    change = int(D[k][2])
    check = int(D[k][6])
    if D[k][5] == "==":
        if valuelist[namelist.index(D[k][4])] == check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    if D[k][5] == "!=":
        if valuelist[namelist.index(D[k][4])] != check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    if D[k][5] == "<=":
        if valuelist[namelist.index(D[k][4])] <= check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    if D[k][5] == ">=":
        if valuelist[namelist.index(D[k][4])] >= check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    if D[k][5] == "<":
        if valuelist[namelist.index(D[k][4])] < check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    if D[k][5] == ">":
        if valuelist[namelist.index(D[k][4])] > check:
            if D[k][1] == "inc":
                valuelist[namelist.index(D[k][0])] += change
            if D[k][1]== "dec":
                valuelist[namelist.index(D[k][0])] -= change
    log.add(max(valuelist))
    
print("Part 1:", max(valuelist))
print("Part 2:", max(log))
