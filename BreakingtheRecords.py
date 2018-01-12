#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    max=0
    min=0
    start=s[0]
    for i in range(n):
        if s[i] > s[0]:
            max+=1
            s[0]=s[i]
    s[0]=start
    for i in range(n):
        if s[i]<s[0]:
            min+=1
            s[0]=s[i]
    return max,min
            
    

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)

print (" ".join(map(str, result)))
