#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count=0
x=0
if len(c)>3:
    while x!=n-3 and x!=n-2:
        if c[x+1]==0 and c[x+2]==1:
            count+=1
            x+=1
        elif c[x+1]==1 and c[x+2]==0:
            count+=1
            x+=2
        elif c[x+1]==0 and c[x+2]==0:
            count+=1
            x+=2
        if x==n-3 or x==n-2:
            count+=1
elif len(c)==3:
    count=1
elif len(c)==2:
    count=1
print(count)
    
    
        