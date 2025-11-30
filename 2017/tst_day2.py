# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:54:23 2019

@author: peder1403
"""

L = [208, 221, 234, 259, 1579, 2542, 3175, 3734, 3806, 3905, 4080, 4225, 4368, 4395, 4464, 4532]

for i in range(len(L)):
        l1 = L[-i]
        for k in range(len(L)-i):
            l2 = L[-(i+k+1)]
            d = l1/l2
            #print(l1 ,l2)
            #print(d)
            if (d).is_integer():
                print(l1, l2)
                print(d)