#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    count=0
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    for i in range(n):
        if a[i]<=0:
            count+=1
    #print(count,k)
    if count>=k:
        print('NO')
    else:
        print('YES')
            