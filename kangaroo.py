#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
x1list=[]
x2list=[]
relative_velocity=v2-v1
distance=x2-x1
if x2>x1 and v2>v1:
    print('NO')
elif x2>x1 or v2>v1:
    if distance!=0:
        if relative_velocity!=0:
            if distance%relative_velocity==0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
    