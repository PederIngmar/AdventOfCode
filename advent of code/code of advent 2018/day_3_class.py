# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 22:25:35 2018

@author: PederIngmar
"""

import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Rect:
    def __init__(self, ll, ur):
        self.ll = ll
        self.ur = ur

    def __str__(self):
        s = "((" + str(self.ll.x) + "," + str(self.ll.y) + ")" 
        s += "(" + str(self.ur.x) + "," + str(self.ur.y) + "))"  
        return s

    def _eq_(self, other):
        return(self.overlap(self, other))

    def overlap(self, other):
        if  other.ll.x < self.ur.x \
        and other.ur.x > self.ll.x \
        and other.ur.y > self.ll.y \
        and other.ll.y < self.ur.y:
            return(True)
        else:
            return(False)
        
    def area(self):
        return (self.ur.x-self.ll.x)*(self.ur.y-self.ll.y)

    def plot(self, c):
        x = []
        y = []
        x.append(self.ll.x)
        x.append(self.ur.x)
        x.append(self.ur.x)
        x.append(self.ll.x)      
        x.append(self.ll.x)
        y.append(self.ll.y)
        y.append(self.ll.y)
        y.append(self.ur.y)
        y.append(self.ur.y)
        y.append(self.ll.y)
        plt.plot(x,y,str(c))
    
### Main ###
data = open('day_3_input.txt').readlines()


sorted_data = []
claimed_points = []

R = []

for linje in data:
    
    n = []
    start = linje.find("@")
    slutt = linje.find(",")
    
    n.append(int(linje[start +1 :slutt]))
    
    
    start = linje.find(",")
    slutt = linje.find(":")
    
    n.append(int(linje[start +1 :slutt]))
    
    start = linje.find(": ")
    slutt = linje.find("x")
    
    n.append(int(linje[start +1 :slutt]))
    
    start = linje.find("x")
    slutt = len(linje)
    
    n.append(int(linje[start +1 :slutt]))
    
    sorted_data.append(n)
    
for linje in sorted_data:   
    a = Point(linje[0],linje[1])
    b = Point(linje[0]+linje[2],linje[1]+linje[3])
    R.append(Rect(a,b))

print("len(R) " + str(len(R)))


j=0
Overlap = []
for r1 in R:
    #print(r)
    r1.plot('r-')
    Overlap.append(0)
    for r2 in R:
        if r1.overlap(r2):
            Overlap[j] +=1
    j +=1
    
#print(Overlap)
for j in range(len(R)):
    if Overlap[j] == 1:
        print(R[j])
        print(j+1)
        R[j].plot('go-')

plt.show()