#!/bin/python3

import sys

def utopianTree(n):
    # Complete this function
    height=1
    if n==0:
        return height
    else:
        i=1
        while(i!=n+1):
            if(i%2==0):
                height+=1
            else:
                height+=height
            i+=1
    return height

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
