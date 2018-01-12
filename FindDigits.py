#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    count=0
    n = int(input().strip())
    string=str(n)
    for i in string:
        if int(i)!=0:
            if n%int(i)==0:
                count+=1
    print(count)
               
