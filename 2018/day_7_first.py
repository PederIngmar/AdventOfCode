# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:00:50 2019

@author: peder1403
"""

data = open("day_7_input.txt").readlines()


S = []

for line in data:
    s = []   
    s.append(line[4 + 1:6])
    s.append(line[-14 + 1:-12])
    S.append(s)

#print(len(S))

rlist = []

while len(S) > 0:
    s2 = []
    S2 = []
    S2.append(S[0])
    s2.append(S[0][0])
    s2.append(S[0][1])
    S.remove(S[0])
    ferdig = 0
    if len(S) == 0:
        ferdig = 1
    k = 0
    while ferdig == 0:
        b1 = S2[k][1]
        e = 0
        while e < len(S):
            b2 = S[e][0]
            if b2 == b1:
                S2.append(S[e])
                s2.append(S[e][1])
                S.remove(S[e])
                e = len(S)
                ferdig = 1
            if e == len(S)-1:
                ferdig = 1

            e += 1
        k += 1
    
    rlist.append(s2)
  
T = [ [i for i in j] for j in rlist]    
#print(len(T))
rlist.sort()
#print(rlist)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

RR = []
while len(rlist) > 0:
    A = []
    for a in alpha:
        m = -1
        for line in rlist: 
            for j in range(len(line)):
                if a == line[j]:
                    if m < j:
                        m = j    
        A.append([m, a])
       
    A.sort()
    Remove = A[0][1]
    print(Remove)
    RR.append(Remove)
    alpha = ''.join([i for i in alpha if i != Remove])
    rlist = [[i for i in j if i!= Remove] for j in rlist]
    for j in range(len(rlist)-1,-1,-1):
        if len(rlist[j]) == 0:
            rlist.pop(j)


print("solution part 1:" + ''.join(RR))       
      


