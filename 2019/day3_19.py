# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:44:03 2019

@author: peder1403
"""

data = open("input_day3_19.txt").read().strip("\n").split("\n")
data[0] = data[0].split(",")
data[1] = data[1].split(",")

D1 = []
D2 = []
for i in data[0]:
    D1.append(i[0])
    D1.append(i[1:])
for i in data[1]:
    D2.append(i[0])
    D2.append(i[1:])   
    


def path(D):
    log = []
    x=0
    y=0
    g = 10000000000
    #log.append((x,y))
    for i in range(0, int(len(D)), 2):
        step = int(D[i+1])
        if D[i] == "R":
            for k in range(step):
                x+=1
                if (abs(x) + abs(y)) < g:
                    log.append((x,y))
        if D[i] == "L":
            for k in range(step):
                x-=1
                if (abs(x) + abs(y)) < g:
                    log.append((x,y))
        if D[i] == "U":
            for k in range(step):
                y+=1
                if (abs(x) + abs(y)) < g:
                    log.append((x,y))
        if D[i] == "D":
            for k in range(step):
                y-=1
                if (abs(x) + abs(y)) < g:
                    log.append((x,y))
            
    return(log)

      
d1 = set(path(D1))
d2 = set(path(D2))
C = d1 & d2
A = [abs(c[0]) + abs(c[1]) for c in C]
print("part 1:", min(A))



"""
for a in range(len(d1)):
    for b in range(len(d2)):
        if d1[a] == d2[b]:
            #A = list(set([x for x in range(len(d1[:a])) if d1[:a].count(d1[:a][x]) == 2]))
            #B = list(set([x for x in range(len(d2[:b])) if d2[:b].count(d2[:b][x]) == 2]))
            #L.append([A, B])
            print("part 2:", a+b)
            #print("part 1:", abs(a[0])+abs(a[1]))
"""   