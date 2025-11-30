# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:48:16 2019

@author: peder1403
"""

data = open("day4_input.txt").read().splitlines()
#print(data)
W = []
invalid = 0
for line in data:
    W.append(line.split())
#print(W)
check = []
for i in range(len(W)):
    for k in range(len(W[i])):
        word = W[i][k]
        for j in range(len(W[i]) - k -1):
            word2 = W[i][k+j+1]
            #print(j,k,i)
            if str(word) == str(word2) :
                #print(W[i])
                #print(word)
                check.append(i)
                invalid += 1


lvalid = []
for i in range(len(check)- 1):
    v1 = check[i]
    v2 = check[i+1]
    if v1 == v2:
        invalid -= 1
    else:
        lvalid.append(v1)
        
print("answer:", len(W) - invalid)



