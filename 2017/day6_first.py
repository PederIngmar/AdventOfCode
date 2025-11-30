# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:21:39 2019

@author: peder1403
"""
from collections import *
input = [14, 0, 15, 12, 11, 11, 3 ,5 ,1, 6, 8, 4, 9, 1, 8, 4, 0]
#input = [5, 6, 7, 8,7,3,5,7,54,3,46,6,6,4,3,23,22,4,4,3,2 ,0]
S = set()
B = list()
B.append(tuple(input))
#print(B)


def largest(B, k):
    s = 0
    for i in range(len(input)-1):
        if B[k][i] > s:
            s = B[k][i]
            pos = i
    return pos

def spred(B, k, pos):
    nlist = list(B[k][:])
    num = nlist[pos]
    nlist[pos] = 0
    i = 1
    while num > 0:
        if pos + i >= len(input)-1:
            i = -pos
        nlist[pos+i] += 1
        num -= 1
        i += 1
    #nlist[-1] +=1
    B.append(tuple(nlist))
    return tuple(nlist)


i = 0
found = False
a = tuple(input[:])
while a not in S and i < 100000:
    S.add(a)
    i+=1
    a = spred(B, -1, largest(B, -1))
    
    """
    for j in range(len(B)-1):
        if B[-1][0:-1] == B[j][0:-1]:
            found = True
            print(j)
            print(B[-1])
            print("-"*50)
        
    i += 1
    """

print(a,i)

"""
#B.sort()
if found:
    for i in range(len(B)):
        print(B[i], sum(B[i][0:-1]))
"""
"""
for i in range(len(B)):
    print(sum(B[i][0:-1]))
"""
   

