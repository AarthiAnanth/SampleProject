#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    list1=[None]*n
    for i in range(n):
        if(list1[ar[i]-1]==None):
            list1[ar[i]-1]=1
        else:
            list1[ar[i]-1]+=1
    max=0
    for i in range(len(list1)):
        if(list1[i]!=None):
            if list1[i]>max:
                max=list1[i]
                value=i+1
    
    return value
            

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
