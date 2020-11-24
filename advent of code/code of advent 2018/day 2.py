# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:17:51 2018

@author: PederIngmar
"""

data = open('box_ID.txt').readlines()

data_2 = 0
data_3 = 0
glob_2 = 0
glob_3 = 0
#print(data[1])

for linje in data:
    box = sorted(linje)
    data_2 = 0
    data_3 = 0
    for i in range(len(box)-2):
        v1 = box[0+i]
        v2 = box[1+i]
        v3 = box[2+i]
        if v2 == v1 and v3 == v1:
            data_3 += 1
            
        elif v2 == v1:
            data_2 += 1
            
    if data_2 > 0:
        glob_2 += 1
     
    if data_3 > 0:
        glob_3 += 1

        
        
print(glob_2)
print(glob_3)
answer = glob_2 * glob_3
print("answer: " + str(answer))
        
        


    
    
    
