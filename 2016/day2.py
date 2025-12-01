# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:16:03 2019

@author: peder1403
"""

data = open("input_day2.txt").read().split()

D = []
for l in data:
	D.append(list(l))

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

X=0
Y=0
code=""
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
	code += str(L[X,Y])

print("part 1:", code)


L2=dict()
L2[(-1,1)] = 2
L2[(0,1)] = 3
L2[(1,1)] = 4
L2[(-1,0)] = 6
L2[(0,0)] = 7
L2[(1,0)] = 8
L2[(-1,-1)] = "A"
L2[(0,-1)] = "B"
L2[(1,-1)] = "C"
L2[(0,-2)]="D"
L2[(0,2)]= 1
L2[(2,0)]=9
L2[(-2,0)]= 5

X=0
Y=0
C=""
for d in D:
	for i in range(len(d)):
		if (d[i] == "U") and (L2[(X,Y)] not in {5,2,1,4,9}):
			Y+=1
		if (d[i] == "D") and (L2[(X,Y)] not in {5,"A","D","C",9}):
			Y-=1
		if (d[i] == "R") and (L2[(X,Y)] not in {"D","C",9,4,1}):
			X+=1
		if (d[i] == "L") and (L2[(X,Y)] not in {1,2,5,"A","D"}):
			X-=1
	C += str(L2[X,Y])

print("part 2:", C)