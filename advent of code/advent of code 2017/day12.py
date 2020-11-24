# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:47:25 2019

@author: peder1403
"""

data = open("day12_input.txt").read().splitlines()

D=[]
for i in range(len(data)):
    e = data[i]
    D.append(e.split(" "))
    D[i].pop(1)
    #D[i].pop(0)
R = []
def f_Tr(D, i, k):
    ##betingelse: #ikke finner den neste     
    f_Tr(D, D[i][k], k+1)
    
    


 
print(D)
