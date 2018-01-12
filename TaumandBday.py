#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    cost=0
    if x==y:
        cost=(b*x)+(w*y)
    elif x<y:
        if z<y:
            if x+z<y:
                cost=(b*x)+((x+z)*w)
            else:
                cost=(b*x)+(w*y) 
        elif y<=z:
            cost=(b*x)+(w*y)
    elif y<x:
        if z<x:
            if y+z<x:
                cost=(w*y)+((y+z)*b)
            else:
                cost=(b*x)+(w*y)
        elif x<=z:
            cost=(b*x)+(w*y)
    print(cost)
        