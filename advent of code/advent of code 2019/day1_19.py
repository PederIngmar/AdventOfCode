# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:45:07 2019

@author: peder1403
"""

data = open("input_day1_19.txt").read().splitlines()
data = list(map(int, data))

sum1 = 0
sum2 = 0
for d in data:
    s =  (d-(d%3))/3 - 2
    sum1 += s
    
    while (s-(s%3))/3 - 2 > 0:
        sum2 += s
        s = (s-(s%3))/3 - 2
    else:
        sum2 += s
        
print("part 1:", int(sum1),"part 2:", int(sum2))

