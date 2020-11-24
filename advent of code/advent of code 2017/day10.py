# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:15:21 2019

@author: peder1403
"""

D = [i for i in range(256)]
lenlist = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]

i = 0
count = 0
skipsize = 0
while count < len(lenlist):
    cpos = D[i]

    if i + lenlist[count] > len(D):
        fliplist1 = D[slice(i, len(D), 1)]
        rest = lenlist[count] - (len(D) - i)
        fliplist2 = D[slice(0, rest, 1)]
        fliplist = fliplist1 + fliplist2
        D1 = D[slice(rest, i, 1)]
        fliplist = list(reversed(fliplist))
        fliplist1 = fliplist[slice(0, len(fliplist)-rest, 1)]
        fliplist2 = fliplist[slice(len(fliplist)-rest, len(fliplist), 1)]
        D = fliplist2 + D1 + fliplist1
        i = rest + skipsize
            
    else:
        fliplist = D[slice(i, i + lenlist[count], 1)]
        D1 = D[slice(0, i, 1)]
        D2 = D[slice(i + lenlist[count], len(D), 1)]    
        fliplist = list(reversed(fliplist))
        D = D1 + fliplist + D2
        i += lenlist[count] + skipsize
    count += 1
    skipsize += 1
print("part 1:",D[0]*D[1])
print(D)

#skipsize#