#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    list2=[]
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            list2.append(s[i])
    if len(list2)==0:
        return 0
    else:
        return len(list2)
        
        

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
