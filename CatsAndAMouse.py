#!/bin/python3

import sys
import math


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if math.fabs(z-x)< math.fabs(z-y):
        print('Cat A')
    elif math.fabs(z-x)>math.fabs(z-y):
        print('Cat B')
    elif math.fabs(z-x)==math.fabs(z-y):
        print('Mouse C')
