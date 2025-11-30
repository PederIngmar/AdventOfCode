# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:08:12 2019

@author: peder1403
"""
import turtle
t = turtle.Turtle()
t.speed(10000)
TS = 1
theinput = 312051
step = 1
while TS < theinput:
    for i in range(2):
        if TS + step > theinput:
            step = theinput - TS    
        t.forward(step)
        t.left(90)
        TS += step

    step += 1

fx = t.xcor()
fy = t.ycor()

print(int(-fx-fy))

turtle.done()

###part 2###
