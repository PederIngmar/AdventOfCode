# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:34:42 2019

@author: peder1403
"""
import time
start_time = time.time()
D = str(open("day11_input.txt").readlines()).split(",")

D[-1] = "ne"
D[0] = "se"

dset = set(D)
dset = list(dset)
m = 0
for i in range(len(D)):
    value = []
    for y in range(len(dset)):
        value.append(D[0:i].count(dset[y]))
    
    nwse = abs(value[dset.index("nw")] - value[dset.index("se")])
    nesw = abs(value[dset.index("ne")] - value[dset.index("sw")])
    ns = abs(value[dset.index("s")] - value[dset.index("n")])
    if m < ns + max(nwse, nesw):
        m = ns + max(nwse, nesw)
print("part 1:", ns + max(nwse, nesw))  
print("part 2:", m)

print("--- %s seconds ---" % (time.time() - start_time))
