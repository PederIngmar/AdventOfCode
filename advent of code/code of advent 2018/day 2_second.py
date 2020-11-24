# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:17:51 2018

@author: PederIngmar
"""

data = open('box_ID.txt').readlines()


for i in range(len(data)-1):
    box_1 = data[0+i]
    for k in range(len(data) - i - 1):
        box_2 = data[k+i+1]
        c = 0
        l = len(box_1) 
        for j in range(len(box_1)):
            if box_2[j] == box_1[j]:
                c += 1
            if c == l-1:
                print(box_1)
                print(box_2)


    
    
    
