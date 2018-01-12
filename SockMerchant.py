#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
temp=[]
count=0
for i in range(n):
    if c[i] not in temp:
        temp.append(c[i])
#print(temp)
for j in temp:
    if c.count(j)%2==0:
        count+=(c.count(j)//2)
    elif (c.count(j)-1)>1 and (c.count(j)-1)%2==0:
        count+=((c.count(j)-1)//2)
print(count)