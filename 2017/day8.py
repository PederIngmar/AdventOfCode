# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:13:00 2019

@author: peder1403
"""

data = open("day8_input.txt").read().splitlines()

D = []

for line in data:
    k = list(line.split())
    D.append(k)
#print(D)


namelist = []
for k in range(len(D)):
    y = 0
    v1 = D[k][0]
    for i in range (len(namelist)):
        v2 = namelist[i]
        if v1 == v2:
            y = 1
    if not y == 1 :        
        namelist.append(v1)
        namelist.append(0)
print(namelist)

def action(name, t, change, ifname, ifset, ifnumb, D, namelist, i):
    namesearch(namelist, D, ifname, name)
    print(k)
"""
    if ifset == "==" :
        if namelist[k+1] == ifnumb:
            if t == "inc":
                namelist[f] += change
            if t == "dec":
                namelist[f] -= change
                
    if ifset == "!=" :
        if namelist[k+1] != ifnumb:
            if t == "inc":
                namelist[f] += change
            if t == "dec":
                namelist[f] -= change
    if ifset == ">" :
        if namelist[k+1] > ifnumb:
            if t == "inc":
                namelist[f] += change
            if t == "dec":
                namelist[f] -= change
    if ifset == "<" :
        if namelist[k+1] < ifnumb:
            if t == "inc":
                namelist[f] += change
            if t == "dec":
                namelist[f] -= change
    if ifset == ">=" :
        if namelist[k+1] >= ifnumb:
            if t == "inc":
                namelist[f] += change
            if t == "dec":
                namelist[f] -= change
    if ifset == "<=" :
        if namelist[k+1] <= ifnumb:
            if t == "inc":
                namelist[i] += change
            if t == "dec":
                namelist[i] -= change
"""
def namesearch(namelist, D, ifname, name):
    for k in range(0, len(namelist), 2):
        if ifname == namelist[k]:
            for f in range(0, len(namelist), 2):
                if name == namelist[k]:
                    return f , k
        

###main###
         
#sizelog = []

for i in range(len(D)):
    name = D[i][0]
    t = D[i][1]
    change = int(D[i][2])
    ifname = D[k][4]
    ifset = D[i][5]
    ifnumb = int(D[i][6])
    
    action(name, t, change, ifname, ifset, ifnumb, D, namelist, i)
    
    
"""
    c = 0
    for j in range(len(namelist)):
        if namelist[j] > c:
            c = namelist[j]
            u = j
    sizelog.append(c)
    #sizelog.append(D[u][0])
print(sizelog)
"""
        
