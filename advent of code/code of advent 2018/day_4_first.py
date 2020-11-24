# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:34:57 2018

@author: PederIngmar
"""
from datetime import datetime
from datetime import timedelta


data = open("day_4_input.txt").readlines()

#guard_number = []

lookfor = "Guard"

info = []
time = []


#sort
for linje in data:
    dates = []
    start = linje.find("[")
    slutt = linje.find("]")
    date = datetime.strptime(linje[start + 1:slutt], '%Y-%m-%d %H:%M')
    time.append(date)
    dates.append(date)
    start = linje.find("]")
    slutt = len(linje)    
    dates.append(str(linje[start + 1:slutt]))
    info.append(dates)


time.sort()
info.sort() 
#print(info)
print("##################################################################################")
#print(time)


key = "asleep"
Guards = []
j = 0
for j in range(len(info)):    
    if lookfor in info[j][1]:
        L_guards = []
        start = info[j][1].find("#")
        slutt =  info[j][1].find("begins")
        guard_number = info[j][1][start + 1:slutt]
        #print(guard_number)
        L_guards.append(guard_number)
        k = j+1
        time_dif = timedelta(minutes=0)
        while lookfor not in info[k][1] and k<len(info)-1:
            if key in info[k][1]:
                time_dif += time[k+1] - time[k]
            k +=1
        #print(time_dif)
        L_guards.append(time_dif)
        Guards.append(L_guards)

Guards.sort()
#print(Guards)

j = 0
k = 0
Guards_distinct = []
while k < len(Guards):
    L_guards = [] 
    sumsleep=timedelta(minutes=0)
    j = k
    while j<len(Guards) and Guards[j][0] == Guards[k][0]:
        sumsleep+=Guards[j][1]
        j+=1
    L_guards.append(sumsleep)
    L_guards.append(Guards[k][0])
    Guards_distinct.append(L_guards)
    k=j

Guards_distinct.sort()    
print(Guards_distinct[len(Guards_distinct)-1])
