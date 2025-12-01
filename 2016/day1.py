# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:07:19 2019

@author: peder1403
"""

data = open("input_day1.txt").read().strip("\n").split(",")


D = []
for d in data:
	d = d.strip(" ")
	D.append([d[0], int(d[1:])])

print(D)
dir = 40
X = 0
Y = 0
log= []
oldX = 0
oldY = 0

log.append((0,0))
for d in D:
	if d[0] == "R":
		dir += 1
	else:
		dir -= 1

	if dir%4 == 0:
		Y+=d[1]
	if dir%4  == 1:
		X+=d[1]
	if dir%4 == 2:
		Y-=d[1]
	if dir%4 == 3:
		X-=d[1]

	for i in range((X-oldX)**0,(X-oldX)**0+(X-oldX),(X-oldX)**0):
		log.append((oldX+i,Y))
	for j in range((Y-oldY)**0,(Y-oldY)**0+(Y-oldY),(Y-oldY)**0):
		log.append((X,oldY+j))

	oldX = X
	oldY = Y


print("Answer part 1:", X+Y)

#print(log)
A = 0
for i in range(1,len(log),1):
	for j in range(i):
		if log[j] == log[i]:
			print(i,j,log[i],log[j], log[i][0]+log[i][1])
			if A ==0:
				A = log[i][0]+log[i][1]
print(log[-1], log[-1][0]+log[-1][1])
print("Answer part 2:", A)








