#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while(len(arr)!=0):
    print(len(arr))
    temp=[]
    min_value=min(arr)
    for i in arr:
        if i !=min_value:
            temp.append(i-min_value)
    arr=temp
