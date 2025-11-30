# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:53:56 2019

@author: peder1403
"""
import re
data = open("day7_input.txt").read().splitlines()
#print(data)

klist = []
for line in data:
    k = re.sub('\?|\(|\)|\-|\>|\,|\:', '', line)
    k = list(k.split())
    #print(k)
    klist.append(k)
#print(klist)

solo = []
many = []

for k in range(len(klist)):
    check = klist[k]
    if len(check) > 2 :
        many.append(check)
    else:
        solo.append(check)
#print(many)

fullist = []
for y in range(len(many)):
    melo = []
    melo.append(many[y][0])
    melo.append(many[y][1])
    fullist.append(melo)

    
def isequal(many, solo, fullist):
    for i in range(len(solo)):
        check = solo[i][0]
        weight = solo[i][1]
        for k in range(len(many)):
            for s in range(2, len(many[k])):
                mcheck = many[k][s]
                if check == mcheck:
                    fullist[k].append(check)           
                    fullist[k].append(weight)
                    #print(check)
    for t in range(len(fullist)):
        if len(fullist[t]) == 2:
            check = fullist[t][0]
            for l in range(len(many)):
                mcheck = many[l][0]
                if check == mcheck:
                    for e in range(2, len(many[l])):
                        check1 = many[l][e]
                        for u in range(len(many)):
                            check2 = many[u][0]
                            weight2 = many[u][1]
                            if check1 == check2:
                                fullist[t].append(check2)           
                                fullist[t].append(weight2)
                                #print(check1,check2,fullist[t])
                         
isequal(many, solo, fullist)
#for i in range(len(fullist)):
print(many[-1], fullist[-1])
    
#print(fullist)

           
 


    