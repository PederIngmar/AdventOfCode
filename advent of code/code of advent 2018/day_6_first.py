# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:46:29 2019

@author: peder1403
"""
import matplotlib.pyplot as plt
data = open("day_6_input.txt").readlines()
#data = open("day_6_input_tst.txt").readlines()
all_points = []
allxy = []
point_list = []
xlist = []
ylist = []
xylist = []
dif_list = []


for line in data:
    xylist = []
    
    start = -1
    slutt = line.find(",")
    xlist.append(int(line[start + 1:slutt]))
    
    start_1 = line.find(" ")
    slutt_1 = len(line)
    ylist.append(int(line[start_1 + 1:slutt_1]))
    
    xylist.append(int(line[start_1 + 1:slutt_1]))
    xylist.append(int(line[start + 1:slutt]))
    
    point_list.append(xylist)

#print(point_list)

def find_shortest(x,y,point_list):
    BIG = 1000000
    shortest = BIG
    shortest_k = -1
    for k in range(len(point_list)):
        x1 = point_list[k][0]
        y1 = point_list[k][1]
        dif = abs(x-x1) + abs(y-y1)
        if dif < shortest:
            shortest = dif
            shortest_k = k
        elif dif == shortest:
            shortest_k = -1
    return shortest_k    
            

MX = 401
MY = 401
M = [[0 for j in range(MX)] for i in  range(MY)]

for x in range(MX):
    for y in range(MY):
            M[x][y] = find_shortest(x, y, point_list) 

BX = 10000 + MX
BY = 10000 + MY
BXM = -10000 - MX
BYM = -10000 - MY

infl = []
for x in range(BXM , BX , 1):
    for y in [BYM , BY]:
        infl.append(find_shortest(x, y, point_list))    
for y in range(BYM , BY , 1):
    for x in [BXM , BX]:
        infl.append(find_shortest(x, y, point_list))
infs = set(infl)
#print(infs)

L = [0 for i in range(len(point_list))]
for x in range(MX):
    for y in range(MY):
        if M[x][y] not in infs:
            L[M[x][y]] += 1
        
L.sort()        
print("solution part 1: " + str(L[-1]))
            
###Del 2###

def find_sum(x,y,point_list):
    S = 0
    for k in range(len(point_list)):
        x1 = point_list[k][0]
        y1 = point_list[k][1]
        S += abs(x-x1) + abs(y-y1)
        
    return S

c = 0
xa = []
ya = []
for x in range(MX):
    for y in range(MY):
        M[x][y] = 0
        s = find_sum(x, y, point_list)
        if s < 10000:
            M[x][y] = s
            c += 1 
            if s > 10000-50: #For plotting
                xa.append(x)
                ya.append(y)


print("solution part 2: " + str(c))

#Plot the pointlist in green and points with infinite area in red and border 
#of area in part 2 with cyan (light blue)
xxl = [xlist[i] for i in range(len(xlist)) if i in infs]
yyl = [ylist[i] for i in range(len(ylist)) if i in infs]
plt.plot(xlist,ylist,'g*')
plt.plot(xxl,yyl,'r*')
plt.plot(xa,ya,'c*')
plt.show()

