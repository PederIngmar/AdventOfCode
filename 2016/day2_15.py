# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:16:03 2019

@author: peder1403
"""

data = open("input_day2.txt").read().split()

D = []
for l in data:
	D.append(list(l))
X=0
Y=0
log=[]
for d in D:
	for i in range(len(d)):
		if (d[i] == "U") and (Y<1):
			Y+=1
		if (d[i] == "D") and (Y>-1):
			Y-=1
		if (d[i] == "R") and (X<1):
			X+=1
		if (d[i] == "L") and (X>-1):
			X-=1
	log.append((X,Y))


L = dict()
L[(-1,1)] = 1
L[(0,1)] = 2
L[(1,1)] = 3
L[(-1,0)] = 4
L[(0,0)] = 5
L[(1,0)] = 6
L[(-1,-1)] = 7
L[(0,-1)] = 8
L[(1,-1)] = 9

code = ""
for l in log:
	code += str(L[l])
print("part 1:", code)
