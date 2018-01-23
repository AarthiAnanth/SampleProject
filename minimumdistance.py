#!/bin/python3

import sys

def minimumDistances(a):
    
    
    min=len(a)
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if i!=j and a[i]==a[j]:
                if abs(i-j)<min:
                    min=abs(i-j) 
    if(min!=len(a)):        
        return min
    else:
        return -1
                
    
            

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    
    result = minimumDistances(a)
    print(result)
