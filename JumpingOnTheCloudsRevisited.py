#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E=100
if n>=2 and n<=25:
    for i in range(0,n,k):
        if c[i]==1:
            E=E-1-2
        elif c[i]==0:
            E=E-1
        
print(E)