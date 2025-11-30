# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:47:22 2018

@author: PederIngmar
"""


data = open('day_3_input.txt').readlines()


sorted_data = []
claimed_points = []

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
    
#print(sorted_data)
    


for linje in sorted_data:
    for i in range(linje[2]):        
        for k in range(linje[3]):
            claimed_points.append((linje[0]+i)*100000+(linje[1]+k))
            
            
## Sort L
L = claimed_points
L.sort()
non_overlap = []
## Check if multiple points come in sequence (used before)
count = 0
j = 0
while j < len(L)-1:
    if L[j+1]==L[j]:
        count += 1
        while L[j+1]==L[j]:
            j += 1
    else:
        non_overlap.append(L[j])
        
    j += 1


# Number of points
print(len(L))

# Number of overlapping points should be 100
print(count)
        
print(non_overlap)
    

