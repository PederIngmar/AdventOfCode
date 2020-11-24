# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:08:12 2019

@author: peder1403
"""

Y = X = 15
M = [ [0 for i in range(X)] for j in range(Y)]

xpos = int(X/2)+1
ypos = int(Y/2)+1
M[ypos][xpos] = 1
y = x = 1

def squaresum(xpos, ypos, check):
    for x1 in range(-1, 2, 1):
        for y1 in range(-1, 2, 1):
            q1 = M[ypos + y1][xpos + x1]
            if not (x1 == 0 and y1 == 0):
                M[ypos][xpos] += q1
    print(M[xpos][ypos])    
    return M[xpos][ypos]

k = 0               
r = 0
check = 312051
while k < int(X/2) and r < check:
    k += 1
    for i in range(k):
        xpos += 1
        r = squaresum(xpos,ypos,check)
   
    for i in range(k):
        ypos -= 1
        r = squaresum(xpos,ypos,check)
   
    k +=1
    for i in range(k):
        xpos -= 1
        r = squaresum(xpos,ypos,check)
   
    for i in range(k):
        ypos += 1
        r = squaresum(xpos,ypos,check)
      
    
    #print(k, r)
#print(r)   
#print(M)