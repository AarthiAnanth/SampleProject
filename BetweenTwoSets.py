#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
a.sort()
b.sort()
temp_list=[]
icount=0
value=0
templist1=[]
#templist1.append(a[-1])
if a[-1]<b[0]:
    for i in range(a[-1],b[0]+1):
        for j in range(n):
            if i%a[j]==0:
                icount+=1
        if icount==n:
            temp_list.append(i)
        icount=0
    xcount=0
    for x in temp_list:

        for k in range(m):
            
            if b[k]%x==0:
                xcount+=1
        if xcount==m:
            
            templist1.append(x)
        xcount=0
    
    #templist1.append(b[0])
    print(len(templist1))
else:
    print(0)

            