# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:37:30 2019

@author: peder1403
"""

data = open("day_8_input.txt").readlines()
K = []
L = data[0].split()
for k in L:
    K.append(int(k))
    
print(K)

s=0
i=0

def jump(N, M):
    global s
    global i
    i += 2
    for j in range(N):
        jump(K[i], K[i+1])
    for k in range(M):
        s  += K[k+i]
    i += M
    


jump(K[0], K[1])
print(s)

"""
meta_count = 0
k = 0
jmps = 2
length = 1

while length > 0:
        jmps = 2
        n_arms = K[k]
        n_meta = K[k+1]
        
        if n_arms == 0:
            for i in range(n_meta):
                meta_count += K[k+2+i]
                #print(K[k+2+i])
            jmps  += n_meta
            
        length -= 1
        length += n_arms
        
        if length <= 0:
            for j in range(k+n_meta+jmps, len(K), 1):
                meta_count += K[j]
                print(n_meta)
                #print(K[j+k])
            length = -1
        k  += jmps
print(meta_count)

S = 0
lz = 0
arm = 0
i = 0
while i != arm:
    K[i*2] = arm
    if arm == 0:
        lz = i*2
        for j in range(K[i+1]):
            S += K[i+2+j]
    i += 1
for i in range(lz+2,len(K),1):
    S += K[i]

print(S)
"""