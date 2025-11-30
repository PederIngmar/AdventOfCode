# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:22:44 2020

@author: peder1403
"""

data = open("input_day6.txt").read().splitlines()

data.sort()
Df = dict()

for i in data:
    d = i.split(")")
    Df[d[1]] = d[0]




def Fstart(s, lim):
    path = []
    while s != lim:
        path.append(s)
        s = Df[s]
    return path

t=0
for i in Df.keys():
    t+=len(Fstart(i, "COM"))
print("del 1:", t)

for i in Fstart("YOU","COM"):
    if i in Fstart("SAN","COM"):
        f = i
        break

steps = len(Fstart("YOU",f))+len(Fstart("SAN",f))
print("del 2:", steps-2)#teller ikke med start og slutt orbitene, bare antall steg mellom
