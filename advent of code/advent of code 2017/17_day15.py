# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:48:51 2019

@author: peder1403
"""
div = 2147483647
startA = 516
startB = 190
faktorA = 16807
faktorB =48271

c = 0
for k in range(40000000):
    startA = (startA*faktorA)%div
    startB = (startB*faktorB)%div
    
    binaryA = bin(startA)
    #for i in range(32-len(binaryA)):
    #    binaryA = "0" + binaryA
    binaryB = bin(startB)
    
    #for i in range(32-len(binaryB)):
    #    binaryB = "0" + binaryB
        
    if binaryA[-16:] == binaryB[-16:]:
        c += 1



print("part 1:", c)
startA = 516
startB = 190
A = []
B = []
c = 0
o = 0
while o < 5000000:
    startA = (startA*faktorA)%div
    startB = (startB*faktorB)%div
    if startA%4 == 0:
        A.append(bin(startA))
        
    #for i in range(32-len(binaryA)):
    #    binaryA = "0" + binaryA
    if startB%8 == 0:
        B.append(bin(startB))
        o += 1
    #for i in range(32-len(binaryB)):
    #    binaryB = "0" + binaryB
    
for i in range(len(B)):
    if A[i][-16:] == B[i][-16:]:
        c += 1


print("part 2:" , c)




